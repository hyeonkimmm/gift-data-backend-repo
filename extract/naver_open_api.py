# -*- coding: utf-8 -*-
# TODO : data 디렉토리에 있는 파일들을 읽어와서 naver shopping api 활용 가격 관련 데이터 수집
# TODO : json 데이터로 저장된 값을
'''
Done : 
1. 특정 키워드 있을 때, 검색 API 활용 쇼핑 데이터 불러오고 전처리 작업
2. 전처리 작업 이후 json 데이터로 저장
'''

# import pandas as pd
# import openpyxl
import requests
import chardet
import json
import re
from pandas import json_normalize
PATH = 'data/info/naver_api_info.json'

# load json data
if __name__ == '__main__':
    with open(PATH, "r") as json_file:
        user_info = json.load(json_file)
        client_id = user_info['client_id']
        client_secret = user_info['client_secret']

def check_utf_8(string):
    return True if chardet.detect(str(string).encode())['encoding'] == 'utf-8' else False


search_word = '원피스'
start_num = 1
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
df['l_price'] = df['mean_price'] - df['std_price']
df['h_price'] = df['mean_price'] + df['std_price']
# top 5 데이터만
df = df.iloc[:5, :]
df.reset_index(inplace=True)
df['index'] = df['index'].apply(lambda x: x + 1)
# 컬럼 정리
df = df[["index", "title", "link", "image", "lprice", "mean_price", "std_price", "l_price", "h_price", "productId", "brand", "maker", "category1", "category2", "category3", "category4"]]
df.rename(columns={'index': 'rank', 'lprice': 'price', 'productId': 'product_id'}, inplace=True)

df.to_json('data_table.json', orient='table', force_ascii=False, index=False)
df.to_json('data.json', orient='columns', force_ascii=False)
df.to_json('data_records.json', orient='records', force_ascii=False)
df.to_json('data_index.json', orient='index', force_ascii=False)
df.to_json('data_split.json', orient='split', force_ascii=False, index=False)
