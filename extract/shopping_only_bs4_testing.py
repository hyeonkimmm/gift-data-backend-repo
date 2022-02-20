# https://curlconverter.com/#
# not used selenium
# 20대 남, 여 , 부모님(50대)
'''
패션의류 50000000
패션잡화 50000001
화장품/미용 50000002
'''
# import os
from random import randint
import time
import requests
import json
import pandas as pd
# 현재 폴더 경로; 작업 폴더 기준
# print(os.getcwd())
MAX_SLEEP_TIME = 10
def get_category():
    headers = {
        'authority': 'datalab.naver.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'accept': '*/*',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://datalab.naver.com/shoppingInsight/sCategory.naver',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'NNB=2IJCMKF7CGJGC; ASID=deee42d50000017da316d7c000000053; _gcl_au=1.1.1014991545.1641950456; NDARK=Y; nid_inf=1919376208; NID_AUT=ft/e+RUZeKnpGd6+phyeSOiJLHJIjRdCCd3GHtDXhPlsYDWLM/XrcO48zKWsoSVt; NID_JKL=U3OTtbyCyDtaUCq3+hC+7/FUWKiwJdUU4sUtkUCiPUQ=; NaverSuggestUse=unuse%26unuse; nx_ssl=2; _ga_4BKHBFKFK0=GS1.1.1643274044.2.1.1643274100.0; _gid=GA1.2.1416298944.1644902405; _ga=GA1.2.1828830193.1637301274; _ga_7VKFYR6RV1=GS1.1.1645008755.99.1.1645008765.50; NID_SES=AAABjjgX4vKrMRaZU+1FYP3Tr2MF8R0+G32gqJy1VqdgRylo8RUNSTSW6i1axt+dHRVen8MXGMS8XmUcrHMyPiHRHtBnGzk6Vqd3chmQztCCCVKos5LxQ5UH3LMA5HCHSDw7neMy4i18MBi0D/vjZ+Ym23XrkALdTM9+lICJHhwMXfyjqSOGtkhh/WL2wxICrQP2Ffd3eGmNixeeTXUwrQ4S7ZFO8xDYCdDXozBYwQDFkDdsBB+/4Ii5NP+QhPbsSIhDuQFgw4EC6gtz2CXJGnquq7I7Vl4K3TXsMdo0ZQhkEy84O6b61rE2zPj4sPIgRRvxMMDLU+Lb9diBQFI5zjZvWBIf86jgXX26O4QkDAHNsTCVG0o4woVw4KWwMbKf2sLfhHCNGLZ0JOp+bFqbfO77pLQy4+wgKVHRLGv3HxbM0RfWA1LDjXZefzDJBv9mEZSsVTiX6XyV3o1yihnhZ/9n0lJYtSp2obWXWrhngB+EmfiyFZIpFKLgN6IraAYtDlX1Z4EBq0BX4OW+O48RkuNPttc=; _datalab_cid=50000000',
    }
    params = (
        ('cid', '50001919'),
    )
    response = requests.get('https://datalab.naver.com/shoppingInsight/getCategory.naver', headers=headers, params=params)
    return response

def crawl_rank(headers, data):
    response = requests.post('https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver', headers=headers, data=data)
    item_list = json.loads(response.text)
    output_file = f"../data/{data['startDate']}_{data['endDate']}_{data['age']}_{data['gender']}_{data['cid']}_{cid_dict[data['cid']].replace('/','&')}.csv"
    df = pd.json_normalize(item_list['ranks'])[['rank', 'keyword']]
    df.to_csv(output_file, index=False)
    # try:
    # df.to_csv(output_dir / output_file)  # can join path elements with / operator
    # except Exception:
    #     print('Error occured!', df)
    #     print(os.getcwd())

headers = {
    'authority': 'datalab.naver.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'accept': '*/*',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://datalab.naver.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://datalab.naver.com/shoppingInsight/sCategory.naver',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=2IJCMKF7CGJGC; ASID=deee42d50000017da316d7c000000053; _gcl_au=1.1.1014991545.1641950456; NDARK=Y; NID_AUT=ft/e+RUZeKnpGd6+phyeSOiJLHJIjRdCCd3GHtDXhPlsYDWLM/XrcO48zKWsoSVt; NID_JKL=U3OTtbyCyDtaUCq3+hC+7/FUWKiwJdUU4sUtkUCiPUQ=; NaverSuggestUse=unuse%26unuse; nx_ssl=2; _ga_4BKHBFKFK0=GS1.1.1643274044.2.1.1643274100.0; _ga=GA1.2.1828830193.1637301274; _ga_7VKFYR6RV1=GS1.1.1645095713.101.1.1645095896.60; _naver_usersession_=ywezCPOHa0aMmFIjIuQgdA==; page_uid=hmb+8sprvTossT5x4wZssssss7G-280424; NID_SES=AAABnW4lsOhOClTwaBizKqHWwdzLRAJctXqnCFDOUWcfoJjKxZDRdLps4VUFYtDR3fMpvUCElSwOamQclfbgiWnrfAx38HXUc6nYjgQjSA1XQT/5PqDezJFz74aBliN39t9KTrvmJz2iM9TQsr1KxGx/2hXshaEf751PIBdQmRvJ1PtYIE6c2Jr8HP/XsMZRL28irIwY/2RCkmZ/i+eiH94YvdAFYKiWB1BLhMb6adA9PeuwuBU78C3YnYVgNZDW/yHIgFJWA8SyJSYfr3diAIQZ1bDSEx2ES/Lw9NWs2t7NI0tHvlAkVKd9y7uNVBXGaJDg5W5Ji8Z5y0+eRWwT+J5atHz0YUiP9BJbHQF24L2fMEYTSEcOefGb4VyrplEexKM0UXRvxGPnCMucTkX0ajmvJF42UurWIu103BRlcE+NBLs8v42A79s20wEtsZn0orHU8zd62uQM16z4bxZxMikuezJxOSis1V2qyw2tXHvWYnCef+/c4WcNU3DHmeHP20zWzl5pVswOdhI59rKmYalH2CZM//cFVe0RgWsO+d3179hj; _datalab_cid=50000000',
}
cid_dict = {'50000000': '패션의류', '50000001': '패션잡화', '50000002': '화장품/미용', '50000003': '디지털/가전'}
# cid_dict = {'50000002': '화장품/미용', '50000003': '디지털/가전'}
# cid_dict = {'50000000': '패션의류', '50000001': '패션잡화'}
age_list = ['20', '50']
gender_list = ['m', 'f']
# cid = '50000002'
# age = '20'
# gender = 'm'

if __name__ == '__main__':
    for cid, item in cid_dict.items():
        for age in age_list:
            for gender in gender_list:
                data = {
                    'cid': f'{cid}',
                    'timeUnit': 'date',
                    'startDate': '2022-02-19',
                    'endDate': '2022-02-19',
                    'age': f'{age}',
                    'gender': f'{gender}',
                    'device': '',
                    'page': '1',
                    'count': '20'
                }
                crawl_rank(headers, data)
                rand_value = randint(1, MAX_SLEEP_TIME)
                time.sleep(rand_value)
                print(f"done {data['startDate']}_{data['endDate']}_{data['age']}_{data['gender']}_{data['cid']}_{cid_dict[data['cid']]}")
