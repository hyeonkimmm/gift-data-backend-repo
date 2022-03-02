# https://curlconverter.com/#
# not used selenium
# 20대 남, 여 , 부모님(50대)
'''
TODO
1. 헤더정보, 카테고리 정보 json에 저장 후 불러오기
2. 자동 디렉토리 생성 코드 작성
'''
import os
from random import randint
import time
import requests
import json
import pandas as pd
from pytz import timezone
from datetime import datetime, timedelta
def get_date(date_type='date', day='yesterday'):
    yesterday = datetime.now(timezone('Asia/Seoul')) - timedelta(1)
    yesterday_date = datetime.strftime(yesterday, '%Y-%m-%d')

    # get today date
    today = datetime.now(timezone('Asia/Seoul'))
    today_date = datetime.strftime(today, '%Y-%m-%d')
    if date_type == 'date':
        if day == 'today':
            return today_date
        elif day == 'yesterday':
            return yesterday_date
    elif date_type == 'datetime':
        if day == 'today':
            return today
        elif day == 'yesterday':
            return yesterday
    else:
        return yesterday, yesterday_date, today, today_date

_PATH = 'data/info/crawl_info.json'
_MAX_SLEEP_TIME = 10
_AGE_LIST = ['20', '50']
_GENDER_LIST = ['m', 'f']

with open(_PATH, "r", encoding='utf-8-sig') as json_file:
    crawl_info = json.load(json_file)
    headers = crawl_info['headers']
    category = crawl_info['root_cat_id']

def crawl_rank(headers, data):
    response = requests.post('https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver', headers=headers, data=data)
    item_list = json.loads(response.text)
    directory = f"data/crawling/{data['age']}_{data['gender']}_{data['cid']}_{category[data['cid']].replace('/','&')}"
    if not os.path.exists(directory):
        os.makedirs(directory)
        print('makedirs ' + f'{directory}')
    output_path = directory + '/' + f"{data['startDate']}_{data['endDate']}.csv"
    df = pd.json_normalize(item_list['ranks'])[['rank', 'keyword']]
    df.to_csv(output_path, index=False)

if __name__ == '__main__':
    date = get_date()
    for cid, item in category.items():
        for age in _AGE_LIST:
            for gender in _GENDER_LIST:
                data = {
                    'cid': f'{cid}',
                    'timeUnit': 'date',
                    'startDate': f'{date}',
                    'endDate': f'{date}',
                    'age': f'{age}',
                    'gender': f'{gender}',
                    'device': '',
                    'page': '1',
                    'count': '20'
                }
                crawl_rank(headers, data)
                rand_value = randint(1, _MAX_SLEEP_TIME)
                time.sleep(rand_value)
                print(f"done {data['startDate']}_{data['endDate']}_{data['age']}_{data['gender']}_{data['cid']}_{category[data['cid']]}")
