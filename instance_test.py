#D:\Python\Python35\python
# -*- coding:utf-8 -*-

import requests
api='http://m.weibo.cn/index/my?format=cards&page=%s'
i=1
url=api % i
r=requests.get(url)
data=r.json()
print(data)
