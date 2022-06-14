import pprint

import requests #리퀘스트설치

url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

pprint.pprint(response.text)