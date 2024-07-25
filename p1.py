#! /usr/bin/python3

import requests

headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'}
params = {"name":"baocongqin","age":"35"}
payload = dict(key1="abc",key2="hahaha")
resp = requests.post('http://www.httpbin.org/post',headers=headers,params=params)
# resp = requests.post('http://www.httpbin.org/post',headers=headers,data=payload)


print(resp.text)
