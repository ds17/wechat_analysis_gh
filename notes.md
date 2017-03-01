## Python<br>
### 2017/2/22
#### 1.获取当前进程工作目录（操作的目录）
```python
os.getcwd()   #get current work direction
```

### 2017/2/23
#### 1.正则表达式元符
　　\d:一个数字；<br>
　　\w：一个字母或数字；<br>
　　\s：一个空格；<br>
　　\S：匹配任意非空字符；<br>
　　.：一个任意字符；<br>
　　*：任意个任意字符；<br>
　　+：一个或以上个任意字符；<br>
　　?：0个或1个任意字符<br>
　　\d+?：加个问号→非贪婪匹配；<br>
　　{n}：n个字符<br>
　　{n,m}：n-m个字符<br>
　　[]：一个范围。
#### 2.正则表达式分组提取<br>
　　在表达式上加()，第一个括号为第一组。<br>
```python
m.group(0)  #原始字符串
m.group(1)  #第一个字符串
```
#### 3.正则表达式编译后直接匹配
```python
re_telephone=re.compile(r'^(\d{3})\-(\d{3-8})$')
re_telephone.match(string)
```
[伯乐在线-正则表达式](http://www.runoob.com/python/python-reg-expressions.html)
#### 4.字符串find
　找到字符返回找到位置索引，未找到返回-1。<br>
#### 5.request请求
```python
r.request(url='https://www.baidu.com')   #获得一个response对象
r.contend   #获得response对象的二进制响应内容。
r.text   #获得解码后的内容。
r.encoding  #获得response对象解码方式
r.encoding='utf-8'  #将response对象解码方式改为：utf-8
```
#### 6.将内容写入文件
先得打开文件，在写入文件，已‘b’形式打开即以'b'形式写入。<br>
```python
with open(filename,'ab') as ff:
    ff.write(bytes)
    ff.close()
```
将request的响应以文件流的形式写入文件
```python
with open(filename, 'ab') as fd:   #ab:二进制形式追加写入
    for chunk in r.iter_content(chunk_size):
        fd.write(chunk)
```
#### 7.进度条显示库
库名：tqdm
#### 8.术语
* UUID:Universally Unique Identifier,通用唯一识别码
* URI：Uniform Resource Identifier
* URN:
　　URI可以分为URL,URN或同时具备locators 和names特性的一个东西。<br>
　　URN作用就好像一个人的名字，URL就像一个人的地址。<br>
　　换句话说：URN确定了东西的身份，URL提供了找到它的方式。<br>

#### 9.调用关联App打开文件
```python
import os
os.startfile(filename)  #win下类似于双击操作。
```
### 2017/2/24
#### 1.HTTP响应代码
  200：请求成功
  201：请求成功并创建一个了新资源
  408：指示客户端没有在服务器准备等待的时间内生成请求
  [响应状态代码Index](http://www.cnblogs.com/lijialong/archive/2011/01/13/http-response-code.html)
#### 2.Win下杀进程
```python
os.system('taskkill /IM dllhost.exe')      #"/IM"前后各有一个空格，加上进程名
os.system('taskkill /F /IM dllhost.exe')   #"/F"强制终止进程
```
进程名：任务管理器 → 应用程序 → 右击  转到进程　
#### 3.解析xml
从xml文件得到dom对象（dom: document object model）
```python
dom1=xml.dom.minidom.parse('xml file path')
```
从xml字符串的得到DOM对象
```python
dom2=xml.dom.minidom.parseString(xmlString)
```
[xml.dom.minidom教程](http://www.cnblogs.com/kaituorensheng/p/4493306.html)
#### 4.import非默认路径下的库
　　新建环境变量：PYTHONPATH,将值设置为库所在目录
###2017/2/26
####1.json数据解码
```python
r=requests.get('url')    #requests得到json数据
data=r.json()    #用json方法解码JSON数据。
#json: javasript object notation 轻量级数据交换格式，一种数据交换语言。
```
####2.pycharm手动安装plugins
下载ZIP文件后可直接安装，下载时需注意对应的pycharm版本。
####3.pycharm快捷键
切换标签：ALT+LEFT/RIGHT<br>
[pycharm快捷键](http://blog.csdn.net/pipisorry/article/details/39909057)
####4.range函数
```python
x=range(1,4)  #只能取得：1,2,3。4是取不到的。
```
###2017/2/28
####1.url的编码问题
按标准，URL只允许一部分ASCII字符，其他字符非法。例如汉字就是非法的。
<br>所以在进行HTTP请求时，将“非法字符”进行编码。
```python
#python 3.x
from urllib import parse
parse.quote(str)  #除了 -._/09AZaz ,都会进行编码
parse.quote_plus(str)   #更激进，也会编码 /
```
####2.进程/线程
一个任务就是一个进程，每个进程可以处理很多种事务，
即多个子任务，子任务成为线程(Tread)。
###2017/3/1
####1.Git代理设置
公司电脑pycharm通过git连接oschina/github提示端口错误，先修改pycharm的代理为公司默认代理设置，再更改git的代理设置。
```python
git config --global http.proxy http://10.237.130.43:2375
git config --global https.proxy http://0.237.130.43:2375
git config --global http.sslverify false 
```
另外在push到github选项中不勾选：Clone git repositories using 

