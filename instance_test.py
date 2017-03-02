#D:\Python\Python35\python
# -*- coding:utf-8 -*-

import requests

url='https://www.google.com.hk'
proxy={'https':'https://127.0.0.1:8087','http': 'http://127.0.0.1:8087'}

try:

    r=requests.get(url,proxies=proxy)
    r.raise_for_status()
    print(r.status_code)
except:
    print('error')