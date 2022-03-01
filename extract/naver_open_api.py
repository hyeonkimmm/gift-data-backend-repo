# -*- coding: utf-8 -*-
# TODO : data 디렉토리에 있는 파일들을 읽어와서 naver shopping api 활용 가격 관련 데이터 수집

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
# lprice 타입 변경
df['lprice'] = df['lprice'].astype('int')
df['mean_price'] = int(df['lprice'].mean())
# top 5 데이터만
df = df.iloc[:5, :]
df.reset_index(inplace=True)
df['index'] = df['index'].apply(lambda x: x + 1)
# 컬럼 정리
df = df[["index", "title", "link", "image", "lprice", "mean_price", "productId", "brand", "maker", "category1", "category2", "category3", "category4"]]
df.rename(columns={'index': 'rank', 'lprice': 'price', 'productId': 'product_id'}, inplace=True)

df.to_json('data.json', orient='table', force_ascii=False, index=False)