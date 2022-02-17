# https://curlconverter.com/#
# not used selenium
import requests
import json
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
    'cookie': 'NNB=2IJCMKF7CGJGC; ASID=deee42d50000017da316d7c000000053; _gcl_au=1.1.1014991545.1641950456; NDARK=Y; nid_inf=1919376208; NID_AUT=ft/e+RUZeKnpGd6+phyeSOiJLHJIjRdCCd3GHtDXhPlsYDWLM/XrcO48zKWsoSVt; NID_JKL=U3OTtbyCyDtaUCq3+hC+7/FUWKiwJdUU4sUtkUCiPUQ=; NaverSuggestUse=unuse%26unuse; nx_ssl=2; _ga_4BKHBFKFK0=GS1.1.1643274044.2.1.1643274100.0; _gid=GA1.2.1416298944.1644902405; _ga=GA1.2.1828830193.1637301274; _ga_7VKFYR6RV1=GS1.1.1645008755.99.1.1645008765.50; _datalab_cid=50000000; NID_SES=AAABk7wX6tLuJuQ5jUtal79ozNM0BU2nKDvZQ017ttnyuP/Djnh2B14POVcxma4ARpP3bKxwJ1iKr7n2RgshMuuZY8iFXYuXUtYl37N3BFwCv1ZDh322e9CwVtg2QUyI+izD9GKZ0u5kix6XfAslHDxxLZNxotSk6RvwBKO/NEmOJpkIjdWR9YEIVZ3nokm91Icyw4tXXxspQ35pWogUqacrDz9Lx/m6HH/e8E80m9Pcimpfprw4SUtD6ijdtXCwIKoz7dc6E596Ja81yx7wMuNjvdJwO6cnICQrfCLXIsemQKrjJaeS+gOdeSQNXwDt+x2tOiGwY732qFmiTScuKJJHn0J6M4ID8KZ6QBXZUcJR03cK67DViFvFHrIbxgQptM1tyge+F0WCUVT+8MseAd1xV9Q2Fz9KJ53xK9VrbnEbGnePZov3l3YG8det/j9MFqzvB9NprPpuq+4/P31awaTg9KPDGm1W41/g1irDLBLbgpwTYowRmUIX7SlpKFQxTa+mFf61OGGgqyQL0UmW2L2X5glbwKpW1LucVwGN9VO5fEKq; page_uid=hlz2mdprvN8ssjII5N0ssssssWw-035626; _naver_usersession_=nz9FIf88xHayI40eChVE3g==',
}

data = {
    'cid': '0',
    'timeUnit': 'date',
    'startDate': '2022-02-16',
    'endDate': '2022-02-16',
    'age': '',
    'gender': '',
    'device': '',
    'page': '1',
    'count': '40'
}
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

# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://datalab.naver.com/shoppingInsight/getCategory.naver?cid=50000000', headers=headers)
response = requests.post('https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver', headers=headers, data=data)
item_list = json.loads(response.text)
item_list['ranks'][0]

item_list.keys()

type(item_list['childList'])
item_list['childList']

cat_dict = {}
for item in item_list['childList']:
    cat_dict[item['cid']] = item['name']

with open('j.json', 'w', encoding='UTF-8-sig') as file:
    file.write(json.dumps(cat_dict, ensure_ascii=False))
