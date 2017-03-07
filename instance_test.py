#D:\Python\Python35\python
# -*- coding:utf-8 -*-
import requests,re
from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt

# import requests
# api='http://m.weibo.cn/index/my?format=cards&page=%s'
# cookies = {
#     "ALF": "xxxx",
#     "SCF": "xxxxxx.",
#     "SUBP": "xxxxx",
#     "SUB": "xxxx",
#     "SUHB": "xxx-", "xx": "xx", "_T_WM": "xxx",
#     "gsScrollPos": "", "H5_INDEX": "0_my", "H5_INDEX_TITLE": "xxx",
#     "M_WEIBOCN_PARAMS": "xxxx"
# }
#
# i=1
# url=api % i
# r=requests.get(url,cookies=cookies)
# r.encoding=r.apparent_encoding
# print(r.encoding)
# # data=r.json()[0]# print(data)
# print(r.text)

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

def get_wordcloud():

    from matplotlib.font_manager import FontProperties
    font=FontProperties(fname='C:\Windows\Fonts\msyh.ttf',size=14)

    text='[今年经济增速目标为何小幅下调？总理这样说！]李克强总理6日上午参加山东代表团审议时说，中国虽然已是11万亿美元的经济体，但仍有条件持续保持经济中高速增长。今年政府工作报告中之所以小幅下调经济增速目标，是为腾出更大空间，用于提高经济质量和效益，加快转型升级，促进中国经济迈向中高端。'
    wordlist=jieba.cut(text,cut_all=False)
    wl_space=' '.join(wordlist)
    my_wordcloud=WordCloud().generate(wl_space)
    plt.imshow(my_wordcloud)
    plt.axis('off',fontproperties=font)
    plt.show()

def matplot_test():
    import numpy as np
    import matplotlib.pyplot as plt

    # from matplotlib.font_manager import FontProperties
    #
    # font=FontProperties(fname='C:\Windows\Fonts\msyh.ttf',size=14)

    x = np.linspace(0, 10, 1000)
    y = np.sin(x)
    z = np.cos(x ** 2)

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
    plt.plot(x, z, "b--", label="$cos(x^2)$")
    plt.xlabel("Time(s)",)
    plt.ylabel("Volt")
    plt.title("PyPlot 第一个例子")
    plt.ylim(-1.2, 1.2)
    plt.legend()
    plt.show()

if __name__=='__main__':
    # matplot_test()
    get_wordcloud()