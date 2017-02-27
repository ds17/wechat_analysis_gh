#D:\Python\Python35\python
# -*- coding:utf-8 -*-

import os,requests,re,time,logging
import xml.dom.minidom
import json,sys,math,subprocess,ssl,threading,urllib

DEBUG=False
global BaseRequest

max_group_num=2
interface_calling_interval=5

QRImagePath=os.path.join(os.getcwd(),'qrcode.jpg')

logfile=os.path.join(os.getcwd(),'wechat_analysis.log')
logging.basicConfig(filename=logfile,level=logging.INFO,format='%(asctime)s %(message)s')


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

BaseRequest={}

contactList=[]
my=[]
SyncKey=[]

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

    logging.info('\n getUUID \n uuid="%s" \n text="%s"' %(uuid,data))

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
    global tip,base_uri,redirect_uri,push_uri
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
        base_uri=redirect_uri[:redirect_uri.rfind('/')]

        services=[
            ('wx2.qq.com', 'webpush2.weixin.qq.com'),
            ('qq.com', 'webpush.weixin.qq.com'),
            ('web1.wechat.com', 'webpush1.wechat.com'),
            ('web2.wechat.com', 'webpush2.wechat.com'),
            ('wechat.com', 'webpush.wechat.com'),
            ('web1.wechatapp.com', 'webpush1.wechatapp.com')
        ]
        push_uri=base_uri
        for (searchUrl,pushUrl) in services:
            if base_uri.find(searchUrl)>=0:
                push_uri='https://%s/cgi-bin/mmwebwx-bin' %pushUrl
                break
        os.system('taskkill /F /IM dllhost.exe')   #杀进程：强制杀，windows照片查看器
    elif code=='408':  #超时
        pass

    return code


def login():
    global skey, wxsid, wxuin, pass_ticket, BaseRequest

    r=myRequests.get(url=redirect_uri)
    r.encoding='utf-8'
    data=r.text

    logging.info('\n loging(): \n xmlString Data:"%s" \n \n \n' %data)

    doc=xml.dom.minidom.parseString(data)
    root=doc.documentElement   #返回xml对象根节点

    for node in root.childNodes:
        if node.nodeName=='skey':
            skey=node.childNodes[0].data
        elif node.nodeName=='wxsid':
            wxsid=node.childNodes[0].data
        elif node.nodeName=='wxuin':
            wxuin=node.childNodes[0].data
        elif node.nodeName=='pass_ticket':
            pass_ticket=node.childNodes[0].data

        logging.info('\n login() \n skey: %s, wxsid: %s, wxuin: %s, pass_ticket: %s \n \n \n' % (skey, wxsid, wxuin, pass_ticket))

    if not all((skey,wxsid,wxuin,pass_ticket)):
        return False

    BaseRequest={
        'Uin': int(wxuin),
        'Sid': wxsid,
        'Skey': skey,
        'DeviceID': deviceID,
    }
    #print(BaseRequest.get('Skey'))
    return True

def webwxinit():
    url=base_uri+'/webwxinit?pass_ticket=%s&skey=%s&r=%s' %(pass_ticket, skey, int(time.time()))
    params={'BaseRequest':BaseRequest}
    headers={'contend-type': 'application/json; charset=UTF-8'}

    r=myRequests.post(url=url,data=json.dumps(params),headers=headers)
    r.encoding='utf-8'
    data=r.json()

    logging.info('webwxinit(): \n json data:',data)

    if DEBUG:
        f=open(os.path.join(os.getcwd(),'webwxinit.json'),'wb')
        f.write(r.content)
        f.close()

    global Contactlist, My ,SyncKey
    dic=data
    Contactlist=dic['ContactList']
    My=dic['User']
    SyncKey=dic['SyncKey']

    state=responseState('webwxinit',dic['BaseResponse'])
    return state

def webwxgetcontact():
    url=(base_uri+'/webwxgetcontact?pass_ticket=%s&skey=%s&r=%s' %(pass_ticket,skey,int(time.time())))
    headers={'content-type':'application/json; charset=UTF-8'}

    r=myRequests.post(url=url,headers=headers)
    data=r.json()

    if DEBUG :
        f=open(os.path.join(os.getcwd(),'webwxgetcontact.json'),'wb')
        f.write(r.content)
        f.close()

    dic=data
    logging.info('contact data:\n',data)
    MemberList=dic['MemberList']

    #倒序遍历,不然删除的时候出问题
    SpecialUsers=["newsapp", "fmessage", "filehelper", "weibo", "qqmail", "tmessage", "qmessage", "qqsync",
                  "floatbottle", "lbsapp", "shakeapp", "medianote", "qqfriend", "readerapp", "blogapp",
                  "facebookapp", "masssendapp", "meishiapp", "feedsapp", "voip", "blogappweixin", "weixin"]
    for i in range(len(MemberList)-1,-1,-1):
        Member=MemberList[i]
        if Member['VerifyFlag'] & 8 !=0 : #公众号/服务号
            MemberList.remove(Member)
        elif Member['UserName'] in SpecialUsers: #特殊账号
            MemberList.remove(Member)
        elif Member['UserName'].find('@@') !=-1: #群聊
            MemberList.remove(Member)
        elif Member['UserName']==My['UserName']: #自己
            MemberList.remove(Member)

    return  MemberList

def syncKey():
    SyncKeyItems=['%s_%s' %(item['Key'],item['Val']) for item in SyncKey['List']]
    SyncKeyStr='|'.join(SyncKeyItems)
    return SyncKeyStr

def syncCheck():
    url=push_uri+'/synccheck?'
    params={
        'sid': BaseRequest['Sid'],
        'skey':BaseRequest['Skey'],
        'uin':BaseRequest['Uin'],
        'deviceId':BaseRequest['DeviceID'],
        'synckey':syncKey(),
        'r':int(time.time()),
    }

    r=myRequests.get(url,params=params)
    r.encoding='utf-8'
    data=r.text

    logging.info('syncCheck data: \n %s' %data)

    regx=r'window.synccheck={retcode:"(\d+)",selector:"(\d+)"}'
    pm=re.search(regx,data)

    retcode=pm.group(1)
    selector=pm.group(2)

    return selector

def webwxsync():
    global SyncKey
    url=base_uri+'/webwxsync?lang=zh_CN&skey=%s&sid=%s&pass_ticket=%s' %(BaseRequest['Skey'],
                                                                         BaseRequest['Sid'], urllib.quote_plus(pass_ticket))
    params={
        'BaseRequest':BaseRequest,
        'SyncKey':SyncKey,
        'rr':~int(time.time()),
    }
    headers={'content-type':'application/json; charset=UTF-8'}

    r=myRequests.post(url=url,data=json.dumps(params))
    r.encoding='utf-8'
    data=r.json()

    dic=data
    SyncKey=dic['SyncKey']

    state=responseState('webwxsync',dic['BaseResponse'])
    return state

def heartBeatLoop():
    while True:
        selector=syncCheck()
        if selector!=0:
            webwxsync()
        time.sleep(1)


def main():
    global myRequests
    if hasattr(ssl, '_create_univerified_context'):
        ssl._create_default_https_context=ssl._create_univerified_context

    headers={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'}
    #Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0

    myRequests=requests.Session()
    myRequests.headers.update(headers)

    if not getUUID():
        print('获取uuid失败')
        return
    print('正在获取二维码图片...')
    showQRImage()

    while waitForLogin() !='200':
        pass

    os.remove(QRImagePath)

    if not login():
        print('登录失败')
        return

    if not webwxinit():
        print('初始化失败')
        return

    Memberlist=webwxgetcontact()

    threading.Thread(target=heartBeatLoop())

    MemberCount=len(Memberlist)
    print('通讯录共%s位好友' %MemberCount)

    d={}
    imageIndex=0
    for Member in Memberlist:
        imageIndex=imageIndex+1
        name='D:\wechat user Image\\'+str(imageIndex)+'.jpg''
        imageUrl='https://wx.qq.com'+Member['HeadImgUrl']
        r=myRequests.get(url=imageUrl,headers=headers)
        imageContent=r.content
        fileImage=open(name,'wb')
        fileImage.write(imageContent)
        fileImage.close()
        print('正在下载第：'+str(imageIndex)+'位好友头像')
        d[Member['UserName']]=(Member['NickName'],Member['RemarkName'])
        city=Member['City']
        city='nocity' if city=='' else city
        name=Member['Nickname']
        name='noname' if name=='' else name
        sign=Member['Signature']
        sign='nosign' if sign=='' else sign
        remark=Member['RemarkName']
        remark='noremark' if remark=='' else remark
        alias=Member['Alias']
        alias='noalias' if alias=='' else alias
        nick=Member['NickName']
        nick='nonick' if nick=='' else nick
        print(name,' ^+*+^ ',city,' ^+*+^ ',Member['Sex'],' ^+*+^ ',Member['StarFriend'],
              ' ^+*+^ ',sign,' ^+*+^ ',remark,' ^+*+^ ',alias,' ^+*+^ ',nick)

if __name__=='__main__':
    main()
    print('回车键退出')
    input()
