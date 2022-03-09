# data lake의 랭킹 정보를 가져와서, 등수를 업데이트 하는 코드
import json
import pandas as pd
import glob
import requests
import re
from pandas import json_normalize
from extract.helper import get_date

def get_api_result(search_word, start_num=1):
    PATH = 'data/info/naver_api_info.json'
    with open(PATH, "r") as json_file:
        user_info = json.load(json_file)
        client_id = user_info['client_id']
        client_secret = user_info['client_secret']
    url = f'https://openapi.naver.com/v1/search/shop.json?query={search_word}&display=100&start={str(start_num)}'
    headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
    res = requests.get(url, headers=headers)
    j = json.loads(res.text)
    df = json_normalize(j['items'])
    # title b 태그 삭제
    df['title'] = df['title'].apply(lambda x: re.sub('<b>|</b>', '', x))
    # link 수정
    df['link'] = 'https://search.shopping.naver.com/catalog/' + df['productId']
    # lprice 타입 변경 및 평균, 표준편차를 통해 최저, 최고 가격 데이터범위 구하기.
    df['lprice'] = df['lprice'].astype('int')
    df['mean_price'] = int(df['lprice'].mean())
    df['std_price'] = int(df['lprice'].std())
    # l_price, h_price - 음수 방지
    df['l_price'] = df[['mean_price', 'std_price']].apply(lambda x: (x[0] - x[1]) if (x[0] - x[1] > 0) else x[0], axis=1)
    df['h_price'] = df['mean_price'] + df['std_price']
    # top 5 데이터만
    df = df.iloc[:5, :]
    df.reset_index(inplace=True)
    df['index'] = df['index'].apply(lambda x: x + 1)
    # 컬럼 정리
    df = df[["index", "title", "link", "image", "lprice", "mean_price", "std_price", "l_price", "h_price", "productId", "brand", "maker", "category1", "category2", "category3", "category4"]]
    df.rename(columns={'index': 'prduct_rank', 'lprice': 'price', 'productId': 'product_id'}, inplace=True)
    df['keyword'] = search_word
    price_df = df[["keyword", "l_price", "h_price"]].iloc[0, :]
    df = df[["prduct_rank", "title", "link", "image", "price", "product_id", "brand", "maker", "category1", "category2", "category3", "category4"]]
    return df, price_df

# 오늘 날짜 구하기
date = get_date(day='today')
all_dir = glob.glob('data/crawling/*')
directory = all_dir[0]
info = directory.split('\\')[1]
age, gender, c_id, c_name = info.split('_')

file_list = glob.glob(directory + '/*')
# TODO : 최신 스코어 점수 업데이트 코드 작성
result = pd.read_csv(file_list[1])
# get top5
result = result.iloc[:5, :].copy()
result.loc[:, 'age'] = age
result.loc[:, 'gender'] = gender
result.loc[:, 'c_id'] = c_id
result.loc[:, 'c_name'] = c_name
result.loc[:, 'date'] = date
result = result[['date', 'rank', 'age', 'gender', 'c_id', 'c_name', 'keyword']]

# result의 keyword를 naver 쇼핑 api를 통해 검색하고 그 결과값을 계속 keyword, product_info 로 정리한 후 더함
merge_df = pd.DataFrame()
for i in range(5):
    key = result.loc[i, 'keyword']
    # 값 불러오기
    df, price_df = get_api_result(key)
    df_dict = df.to_dict(orient='records')
    # df_json = df.to_json(orient='records', force_ascii=False)
    price_df['product_info'] = df_dict
    merge_df = pd.concat([merge_df, price_df], axis=1)
merge_df = merge_df.transpose()
result = pd.merge(result, merge_df, how='left', on='keyword')
result['rank'] = result['rank'].astype(object)
a = result.to_dict(orient='records')
# result.to_dict(orient='index')
# dict(result.to_dict(orient='records'))
final = dict()
final['data'] = a
