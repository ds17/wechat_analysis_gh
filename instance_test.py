#D:\Python\Python35\python
# -*- coding:utf-8 -*-
import requests,re

def get_sina():
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

def get_baidu():
    url='https://www.baidu.com/s?'
    params={'wd':'python'}
    headers={'user-agent':'Mozilla/5.0'}
    try:
        r=requests.get(url,params=params,timeout=10,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print(r.headers)
        print(r.encoding)

    except:
        print('爬取异常')

def get_so():
    url='https://www.so.com/s?'
    kw={'q':'python'}
    user_agent={'user-agent':'Mozilla/5.0'}
    try:
        r=requests.get(url,params=kw,headers=user_agent)
        r.raise_for_status()
        r.encoding='utf-8'
        print(r.text[:2000])
    except:
        print('爬取异常')

def get_pic():
    url='https://imgsa.baidu.com/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=d3c32eb1213fb80e18dc698557b8444b/0eb30f2442a7d9331abfc6f3ad4bd11373f0011e.jpg'

    try:
        r = requests.get(url)
        r.raise_for_status()
        with open('python.jpg','wb') as f:
            f.write(r.content)
            f.close()
    except:
        print('爬取异常')

def short_url():
    #http://suo.im/api.php?format=json&url=http://www.baidu.com
    url='https://imgsa.baidu.com/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=d3c32eb1213fb80e18dc698557b8444b/0eb30f2442a7d9331abfc6f3ad4bd11373f0011e.jpg'
    short_tool='http://suo.im/api.php?format=json&url='
    r=requests.get(url=short_tool+url)
    short_dic=r.json()
    return short_dic['url']

def phone_loc():
    number = input('请输入手机号：')
    number=str(number)
    url='http://m.ip138.com/mobile.asp?'
    kw={'mobile':number}
    try:
        r=requests.get(url,params=kw)
        r.raise_for_status()
        r.encoding='utf-8'
        contend=r.text
        # print(contend)
        location=re.search(r'卡号归属地</td><td><span>(.*?)</span>',contend)
        print('归属地：'+location.group(1))

    except:
        print('爬取error')

def bs_test():
    from bs4 import BeautifulSoup
    url='http://python123.io/ws/demo.html'
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    print(soup.p.string)


if __name__=='__main__':
    # phone_loc()
    bs_test()
