#D:\Python\Python35\python
# -*- coding:utf-8 -*-

import requests

# cookies={'SUBP':'0033WrSXqPxfM725Ws9jqgMF55529P9D9WFRfCfNcNcXm1B7_Wd1oVcK5JpX5K2hUgL.Fozc1Kzc1hM01hz2dJLoIpHZMLYLxK-LBo5L12qLxKnL1K.LB-zt',
#          'SUHB':'0YhAdlIqovEs4d',
#          'UOR':'soft.yesky.com,widget.weibo.com,www.baidu.com',
#          'SINAGLOBAL':'5319814165810.406.1461732834304',
#          'ULV':'1489190559721:65:9:5:4259012788872.0454.1489190559530:1489117731808',
#          'SCF':'AlDNHv7-FnOqek_jVZZf73TmTX2uYz4Ew4hrTzQgESW1GrQw_Ma7Ytp_pXUGe7cg_iRDONB2cRlCDfbIThNlWRM.',
#          'wb_g_upvideo_2692687382':'1',
#          'un':'ryan_jin@sina.com',
#          '_s_tentry':'www.liaoxuefeng.com',
#          'Apache':'4259012788872.0454.1489190559530',
#          'YF-Ugrow-G0':'3a02f95fa8b3c9dc73c74bc9f2ca4fc6',
#          'login_sid_t':'c9b5f74e0975a8b47a21b3b3e870f8e0',
#          'YF-V5-G0':'a906819fa00f96cf7912e89aa1628751',
#          'ALF':'1520752594',
#          'SSOLoginState':'1489216595',
#          'wvr':'6',
#          'YF-Page-G0':'aabeaa17d9557111c805fb15a9959531',
# }
cookies={'ALF':'1520752594',
         'SCF':'AlDNHv7-FnOqek_jVZZf73TmTX2uYz4Ew4hrTzQgESW1GrQw_Ma7Ytp_pXUGe7cg_iRDONB2cRlCDfbIThNlWRM.',


}

def fetch_weibo():
    api='http://m.weibo.cn/index/my?format=cards&page=1'
    # for i in range(1,2):
    #     r=requests.get(url=api %i, cookies=cookies)
    #     r.encoding=r.apparent_encoding
    #     print(r.text)
        # data=r.json()[0]
        # print(data)
    r = requests.get(url=api, cookies=cookies)
    r.encoding=r.apparent_encoding
    print(r.text)

if __name__=='__main__':
    fetch_weibo()



