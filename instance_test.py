#D:\Python\Python35\python
# -*- coding:utf-8 -*-

import requests
api='http://m.weibo.cn/index/my?format=cards&page=%s'
cookies = {
    "ALF": "xxxx",
    "SCF": "xxxxxx.",
    "SUBP": "xxxxx",
    "SUB": "xxxx",
    "SUHB": "xxx-", "xx": "xx", "_T_WM": "xxx",
    "gsScrollPos": "", "H5_INDEX": "0_my", "H5_INDEX_TITLE": "xxx",
    "M_WEIBOCN_PARAMS": "xxxx"
}

i=1
url=api % i
r=requests.get(url,cookies=cookies)
r.encoding=r.apparent_encoding
print(r.encoding)
# data=r.json()[0]# print(data)
print(r.text)