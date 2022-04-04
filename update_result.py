# 디렉토리 별 최신 스코어 불러와서, firebase 업데이트 데이터 만들기
import json
import pandas as pd
import requests
import re
import glob
from update_score import get_top_rank
from pandas import json_normalize

_TOP_RANK = 20
PATH = 'data/info/naver_api_info.json'
with open(PATH, "r") as json_file:
    user_info = json.load(json_file)
    _CLIENT_ID = user_info['client_id']
    _CLIENT_SECRET = user_info['client_secret']
_HEADERS = {"X-Naver-Client-Id": _CLIENT_ID, "X-Naver-Client-Secret": _CLIENT_SECRET}

def get_api_result(search_word='원피스', start_num=1):
    search_url = f'https://openapi.naver.com/v1/search/shop.json?query={search_word}&display=100&start={str(start_num)}'
    web_url = f'https://search.shopping.naver.com/search/all?query={search_word}&cat_id=&frm=NVSHATC'
    json_res = json.loads(requests.get(search_url, headers=_HEADERS).text)
    df = json_normalize(json_res['items'])
    if len(df.index) < 5:
        return None
    # title b 태그 삭제
    df['title'] = df['title'].apply(lambda x: re.sub('<b>|</b>', '', x))
    # link 수정
    df['link'] = 'https://search.shopping.naver.com/catalog/' + df['productId']
    # lprice 타입 변경 및 평균, 표준편차를 통해 최저, 최고 가격 데이터범위 구하기.
    df['lprice'] = df['lprice'].astype('int').fillna(0)
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
    appInfo = df[["keyword", "lowPrice", "highPrice", "meanPrice"]].iloc[0, :]
    appInfo['webUrl'] = web_url
    appInfo['imageUrl'] = df.loc[0, 'image']
    df = df[["keyword", "productRank", "title", "link", "image", "productPrice", "productId", "brand", "maker", "category1", "category2", "category3", "category4"]]
    appInfo['productInfo'] = df.to_dict(orient='records')
    return (df, appInfo)

def update_today_best(path):
    score_path = path + '/score.csv'
    result = get_top_rank(score_path)
    result = result[['rank', 'keyword', 'score']]
    merge_df = pd.DataFrame()
    '''
    1. result의 key 값을 넘긴다.
    2. key값을 해당 함수를 통과시켜 결과값을 받아냄.
    3. 해당 결과값을 result에 차곡차곡 쌓는다.
    pandas apply를 활용 시간 효율성 증가.
    '''
    # merge_product = pd.DataFrame()
    keyword_count = 0
    while keyword_count <= _TOP_RANK:
        try:
            key = result.loc[keyword_count, 'keyword']
            # 값 불러오기
            func_result = get_api_result(key)
            if func_result:
                productInfo, appInfo = func_result
            else:
                continue
        except Exception:
            print(f'error {key}, {path}')
            raise ValueError
        merge_df = pd.concat([merge_df, appInfo], axis=1)
        # df_dict = productInfo.to_dict(orient='records')
        # merge_product = pd.merge(productInfo, merge_product)
    merge_df = merge_df.transpose()
    merge_df.reset_index(drop=True, inplace=True)
    result = pd.merge(result, merge_df, how='left', on='keyword')
    result.rename(columns={'keyword': 'keyWord'}, inplace=True)
    result.to_csv(path + '/today_best.csv')
    # productInfo.to_csv(path + '/today_best_product.csv')


# result의 keyword를 naver 쇼핑 api를 통해 검색하고 그 결과값을 계속 keyword, product_info 로 정리한 후 더함
if __name__ == '__main__':
    all_dir = glob.glob('data/crawling/*')
    for path in all_dir:
        update_today_best(path)
        print(f'updated successfully {path}')
