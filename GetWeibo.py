#D:\Python\Python35\python
# -*- coding:utf-8 -*-

import requests,re,csv

# cookies={'ALF':'1520752594',
#          'SCF':'AlDNHv7-FnOqek_jVZZf73TmTX2uYz4Ew4hrTzQgESW1GrQw_Ma7Ytp_pXUGe7cg_iRDONB2cRlCDfbIThNlWRM.',
#          'SSOLoginState':'1489216595',
#          'SUB':'_2A251x9QDDeTxGeRI4lAX-CnPwz6IHXVWtULLrDV8PUNbmtBeLWL-kW94uj3hg2tVbGJAw1Z-R0p4ajXLag..',
#          'SUBP':'0033WrSXqPxfM725Ws9jqgMF55529P9D9WFRfCfNcNcXm1B7_Wd1oVcK5JpX5K2hUgL.Fozc1Kzc1hM01hz2dJLoIpHZMLYLxK-LBo5L12qLxKnL1K.LB-zt',
#          'SUHB':'0YhAdlIqovEs4d',
#          '_T_WM':'1f22f9f63f5fa9d3029896ebf2e19544',
# }
def get_cookie():
    cookies = {}
    filePath=r'd:\cookies\getweibo cookie.txt'
    file=open(filePath,'r')
    text=file.read()
    regx='(\w.*?)=(.*?);'
    items=re.findall(regx,text)
    for item in items:
        cookies[item[0]]=item[1]
    return cookies

cookies=get_cookie()

def fetch_weibo():
    api='http://m.weibo.cn/index/my?format=cards&page=%s'

    def clean(text):
        regx=r'<a .*?/a>|<i .*?/i>|转发微博|//|Repost|，|？|。|、|分享图片|（|）|(|)|：|:|&quot;'
        content=re.sub(regx,'',text)
        return content

    for i in range(1,100):
        r = requests.get(url=api %i, cookies=cookies)
        # r.encoding='gbk'  #r.apparent_encoding
        data=r.json()[0]
        # print(data)
        groups=data.get('card_group') or []

        for group in groups:
            text=group.get('mblog').get('text')
            text=clean(text)
            if text:
                yield(text)


def claen_text():
    for text in fetch_weibo():
        text=re.sub('\u200b|','',text)
        if text:
            yield text

def write_csv(texts):
    file=open('./weibo.csv','w',newline='')
    writter=csv.writer(file)
    for text in texts:
        writter.writerow([text])
    file.close()

if __name__=='__main__':
    texts=claen_text()
    write_csv(texts)




