#D:\Python\Python35\python
# -*- coding:utf-8 -*-
import requests,re,csv

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
    # url='http://python123.io/ws/demo.html'
    url='http://www.dysfz.net/'
    r=requests.get(url)
    r.encoding=r.apparent_encoding
    soup=BeautifulSoup(r.text,'html.parser')

    for link in soup('a'):
        link_attr=link.get('href')
        if re.match('http',link_attr):
            print(link_attr)
    # for tag in soup.a.next_siblings:
    #     print(tag)

def codes_test():
    a='风卷残云'
    print(type(a))
    # b=a.encode('utf-8')
    # print(b)
    # print(type(b))




def csv_test():
    file_path=r'C:\Users\SP52479\Desktop\AQI计算.csv'
    file=open(file_path,'r+',newline='\n')
    reader=csv.reader(file)
    writer=csv.writer(file)
    data=[]
    for line in reader:
        data.append(line)
    writer.writerow(['python2','write2','csv2','test2'])
    writer.writerow(['value1','value2'])

def json_test():
    import json
    filepath=r'C:\Users\SP52479\Desktop\test.json'
    file=open(filepath,'r')
    data=json.load(file)

def sa_before_tax():
    base=float(input('Input Salary per month:'))
    month_get=base * (1-0.175)
    total_wage=month_get * 12  + base * 4
    sa_before=total_wage / 12 / (1-0.175)
    print('sa_before:',float('%.2f' %sa_before))

def format_test():
    tplt='i\'m {0}{{and}}'
    print(tplt.format('test '))

def csv_dic():
    f_p=r'C:\Users\SP52479\Desktop\AQI计算.csv'
    file=open(f_p,'r+',newline='')
    reader=csv.DictReader(file,fieldnames=['A','B','C','D','E','F','G'],restkey='空')
    file_dict=[]
    for row in reader:
        # file_dict.append(row)
        print(row)
    file.close()
    # print(file_dict)

def class_test():
    class Student(object):
        __slots__=('name','age')
        def __init__(self,name,age):
            self.name=name
            self.age=age

        def print_info(self):
            print('%s is %s years old' %(self.name,self.age))

        def get_grade(self):
            if self.age<30:
                return 'young'
            elif self.age<50:
                return 'Middle'
            else:
                return 'old'
        # def set_score(self,score):
        #     self.score=score

    bob=Student('bab kaka',36)

    # from types import MethodType
    # bob.set_score=MethodType(set_score,bob)
    # bob.set_score(66)
    # print(getattr(bob,'score'))
    # bob._Student__name='richard jin'
    # bob.print_info()

def jieba_test():
    import jieba.analyse

    text='每个txt文件夹里面存放一个用户的全部微博数据，在result_all文件里面存放了全部用户的微博数据，这里实现读取每个用户的数据并为每个用户提取30个关键字。将为每个用户提取出来的关键字存放在同一个文件topic_all.txt文件里面。'
    keywords=jieba.analyse.extract_tags(text)
    print(keywords)

def ana_test():
    import time
    print(time.time())

def ocdb_test():
    import pyodbc
    dbfile=r'X:\sect1\2 试验数据\RAC\17S\NS\一次设试\NS12 试验数据\3.14\暖房定格\cav20170314_100749_1.mdb'
    conn=pyodbc.connect(r'Drivers={Microsoft Access Driver(*.mdb,*.accdb)};DBQ='+dbfile +';Uid=;Pwd=;')
    cursor=conn.cursor
    SQL='SLECT * from table1;'
    for row in cursor.excute(SQL):
        print (row.coll)
    cursor.close()
    conn.close()

def press_exit():
    input('按Enter建退出：')

if __name__=='__main__':
    # phone_loc()
    # bs_test()
    # csv_test()
    # json_test()
    # sa_before_tax()
    # format_test()
    # csv_dic()
    # class_test()
    # jieba_test()
    # codes_test()
    # ocdb_test()
    press_exit()
