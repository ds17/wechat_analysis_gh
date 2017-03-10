#D:\Python\Python35\python
# -*- coding:utf-8 -*-
'python课程实例：爬取大学列表'


import requests,bs4
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding

        return r.text
    except:
        print('get HTML ERROR')

def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])


def printUnivlist(ulist,num):
    print('{:^5}\t{:<20}\t{:<6}\t{:>10}'.format('排名','学校名称','省市','总分'))
    for i in range(num):
        u=ulist[i]
        print('{:^5}\t{:<20}\t{:<6}\t{:>10}'.format(u[0],u[1],u[2],u[3]))


def main():
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    uinfo=[]
    html=getHTMLText(url)

    fillUnivList(uinfo,html)
    printUnivlist(uinfo,20) # 20 univs


main()

