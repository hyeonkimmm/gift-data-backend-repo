# 디렉토리 별 최신 스코어 불러와서, firebase 업데이트 데이터 만들기
import json
import pandas as pd
import requests
import re
import glob
from update_score import get_top5_rank
from pandas import json_normalize

def get_api_result(search_word='원피스', start_num=1):
    PATH = 'data/info/naver_api_info.json'
    with open(PATH, "r") as json_file:
        user_info = json.load(json_file)
        client_id = user_info['client_id']
        client_secret = user_info['client_secret']
    url = f'https://openapi.naver.com/v1/search/shop.json?query={search_word}&display=100&start={str(start_num)}'
    # 검색용 url
    web_url = f'https://search.shopping.naver.com/search/all?query={search_word}&cat_id=&frm=NVSHATC'
    headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
    res = requests.get(url, headers=headers)
    j = json.loads(res.text)
    df = json_normalize(j['items'])
    # title b 태그 삭제
    df['title'] = df['title'].apply(lambda x: re.sub('<b>|</b>', '', x))
    # link 수정
    df['link'] = 'https://search.shopping.naver.com/catalog/' + df['productId']
    # lprice 타입 변경 및 평균, 표준편차를 통해 최저, 최고 가격 데이터범위 구하기.
    df['lprice'] = df['lprice'].astype('int').fillna(0)
    # TODO: ValueError: cannot convert float NaN to integer 에러 해결 (NaN 처리 해주기)
    # TODO: 검색 결과가 없거나 적은 경우
    df['meanPrice'] = int(df['lprice'].mean())
    df['stdPrice'] = int(df['lprice'].std())
    # lowPrice - 음수 방지
    df['lowPrice'] = df[['meanPrice', 'stdPrice']].apply(lambda x: (x[0] - x[1]) if (x[0] - x[1] > 0) else x[0], axis=1)
    df['highPrice'] = df['meanPrice'] + df['stdPrice']
    # top 5 데이터만
    df = df.iloc[:5, :]
    df.reset_index(inplace=True)
    df['index'] = df['index'].apply(lambda x: x + 1)
    # 컬럼 정리
    df = df[["index", "title", "link", "image", "lprice", "meanPrice", "stdPrice", "lowPrice", "highPrice", "productId", "brand", "maker", "category1", "category2", "category3", "category4"]]
    df.rename(columns={'index': 'productRank', 'lprice': 'productPrice'}, inplace=True)
    df['keyword'] = search_word
    appInfo = df[["keyword", "lowPrice", "highPrice"]].iloc[0, :]
    appInfo['webUrl'] = web_url
    appInfo['imageUrl'] = df.loc[0, 'image']
    df = df[["productRank", "title", "link", "image", "productPrice", "productId", "brand", "maker", "category1", "category2", "category3", "category4"]]
    return df, appInfo

def update_today_best(path):
    score_path = path + '/score.csv'
    result = get_top5_rank(score_path)
    result = result[['rank', 'keyword', 'score']]
    merge_df = pd.DataFrame()
    for i in range(5):
        try:
            key = result.loc[i, 'keyword']
            # 값 불러오기
            df, appInfo = get_api_result(key)
        except Exception:
            print(f'error {key}, {path}')
            raise ValueError
        # df_dict = df.to_dict(orient='records')
        # df_json = df.to_json(orient='records', force_ascii=False)
        # appInfo['product_info'] = df_dict
        merge_df = pd.concat([merge_df, appInfo], axis=1)
    merge_df = merge_df.transpose()
    merge_df.reset_index(drop=True, inplace=True)
    result = pd.merge(result, merge_df, how='left', on='keyword')
    result.rename(columns={'keyword': 'keyWord'}, inplace=True)
    result.to_csv(path + '/today_best.csv')
    df.to_csv(path + '/today_best_product.csv')


# result의 keyword를 naver 쇼핑 api를 통해 검색하고 그 결과값을 계속 keyword, product_info 로 정리한 후 더함
if __name__ == '__main__':
    all_dir = glob.glob('data/crawling/*')
    for path in all_dir:
        update_today_best(path)
        print(f'updated successfully {path}')
