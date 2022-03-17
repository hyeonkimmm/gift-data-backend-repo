# 네이버 쇼핑 인사이트 기준 모든 카테고리 id 불러오는 코드
# robots.txt 기준 준수 + 크롤링 중간에 SLEEP_TIME 설정
# 2022-02-17 hkim
import requests
import json
from collections import deque
from random import randint
import time
MAX_SLEEP_TIME = 10
# 임시 함수
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
params = [
    ['cid', 0],
]
class req_cat:
    def __init__(self, headers, params) -> None:
        self.cat_dict = {}
        self.headers = headers
        self.params = params
        self.update = deque(['0'])
        self.done = set()

    def set_cat_id(self, cat_id):
        self.params[0][1] = cat_id

    def update_cat_id(self):
        response = requests.get('https://datalab.naver.com/shoppingInsight/getCategory.naver', headers=self.headers, params=self.params)
        item = json.loads(response.text)
        for child in item['childList']:
            cid = child['cid']
            name = child['name']
            if cid in self.done:
                continue
            self.cat_dict[cid] = name
            self.update.append((cid))
        self.done.add(item['cid'])

if __name__ == '__main__':
    cat = req_cat(headers, params)
    while cat.update:
        cat_id = cat.update.popleft()
        cat.set_cat_id(cat_id)
        # TODO: 에러 발생 시 트래픽 처리 및 데이터 정리
        try:
            cat.update_cat_id()
        except BaseException:
            time.sleep(10)
        print(cat_id)
        rand_value = randint(1, MAX_SLEEP_TIME)
        time.sleep(rand_value)

    with open('cat_id.json', 'w', encoding='UTF-8-sig') as file:
        file.write(json.dumps(cat.cat_dict, ensure_ascii=False))
