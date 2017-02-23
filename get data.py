#D:\Python\Python35\python
# -*- coding:utf-8 -*-

import os,requests,re,time
import xml.dom.minidom
import json,sys,math,subprocess,ssl,threading,urllib

DEBUG=False

max_group_num=2
interface_calling_interval=5

QRImagePath=os.path.join(os.getcwd(),'qrcode.jpg')

tip=0
uuid=''

base_uri=''
redirect_uri=''
push_uri=''

skey=''
wxsid=''
wxuin=''
pass_ticket=''
deviceID='e000000000000000'

baseRequest={}

contactList=[]
my=[]
syncKey=[]

def responseState(func,BaseResponse):
    ErrMsg=BaseResponse['ErrMsg']
    Ret=BaseResponse['Ret']
    if DEBUG or Ret !=0:
        print('func: %s, Ret: %d, ErrMsg: %s' %(func,Ret,ErrMsg))

    if Ret !=0:
        return False
    return True

def getUUID():
    global uuid
    url='https://login.weixin.qq.com/jslogin'
    params={
        'appid':'wx782c26e4c19acffb',
        'fun':'new',
        'lang':'zh_CN',
        '_':int(time.time())
    }

    r=myRequests.get(url=url, params=params)
    r.encoding='utf-8'
    data=r.text
    regx = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)"'
    pm=re.search(regx,data)
    code=pm.group(1)
    uuid=pm.group(2)

    if code=='200':
        return True
    return False

def showQRImage():
    global tip

    url='https://login.weixin.qq.com/qrcode/' + uuid
    params={
        't':'webwx',
        '_':int(time.time())
    }

    r=myRequests.get(url=url,params=params)

    tip=1

    f=open(QRImagePath,'wb')
    f.write(r.content)
    f.close()
    time.sleep(1)

    if sys.platform.find('darwin')>=0:
        subprocess.call(['open',QRImagePath])  #MAC下打开文件
    elif sys.platform.find('win32')>=0:
        os.startfile(QRImagePath)     #Win下打开文件
    else:
        subprocess.call(['xdg-open',QRImagePath])     #Linux下打开文件

    print('请使用维修扫描二维码登录')

def waitForLogin():
    global tip,base_url,redirect_url,push_url
    url='https://login.weixin.qq.com/cgi-bin/mmwebwx-bin/login?tip=%s&uuid=%s&_=%s' %(tip,uuid,int(time.time()))
    r=myRequests.get(url=url)
    r.encoding='utf-8'
    data=r.text
    regx=r'window.code=(\d+);'
    pm=re.search(regx,data)

    code=pm.group(1)

    if code=='201':  #已扫描
        print('成功扫描，请在手机上确认以登录')
        tip=0
    elif code=='200':  #已登录
        print('正在登录...')
        regx=r'window.redirect_uri="(\S+?)";'
        pm=re.search(regx,data)
        redirect_uri=pm.group(1)+'&fun=new'






def main():
    global myRequests



    myRequests=requests.Session()





