#D:\Python\Python35\python
# -*- coding:utf-8 -*-

import requests

cookies={'ALF':'1520752594',
         'SCF':'AlDNHv7-FnOqek_jVZZf73TmTX2uYz4Ew4hrTzQgESW1GrQw_Ma7Ytp_pXUGe7cg_iRDONB2cRlCDfbIThNlWRM.',
         'SSOLoginState':'1489216595',
         'SUB':'_2A251x9QDDeTxGeRI4lAX-CnPwz6IHXVWtULLrDV8PUNbmtBeLWL-kW94uj3hg2tVbGJAw1Z-R0p4ajXLag..',
         'SUBP':'0033WrSXqPxfM725Ws9jqgMF55529P9D9WFRfCfNcNcXm1B7_Wd1oVcK5JpX5K2hUgL.Fozc1Kzc1hM01hz2dJLoIpHZMLYLxK-LBo5L12qLxKnL1K.LB-zt',
         'SUHB':'0YhAdlIqovEs4d',
         '_T_WM':'1f22f9f63f5fa9d3029896ebf2e19544',
}

def fetch_weibo():
    api='http://m.weibo.cn/index/my?format=cards&page=%s'
    for i in range(1,100):
        r = requests.get(url=api %i, cookies=cookies)
        r.encoding=r.apparent_encoding
        data=r.json()[0]


if __name__=='__main__':
    fetch_weibo()



