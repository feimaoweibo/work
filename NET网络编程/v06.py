# FTP编程案例
import ftplib # 关于FTP的操作都在此包中
import os
import socket

# 三部分精确表示在FTP服务器上的某一个文件
HOST = "ftp.acc.umu.se"
DIR = 'Public/EFLIB/'
FILE = 'README'

# 1、客户端链接远程主机上的FTP服务器
try:
    f = ftplib.FTP()
    # 通过设置调式级别可以方便调式
    f.set_debuglevel(2)
    # 链接主机地址
    f.connect(HOST)
except Exception as e:
    print(e)
    exit()
print("客户端请求链接***大学FTP服务器地址{0}".format(HOST))

# 2、客户端输入用户名和密码（或者‘anonymous’和电子邮件地址）
try:
    # 登陆如果没有输入用户信息，则默认使用匿名登陆
    f.login()
except Exception as e:
    print(e)
    exit()
print("该用户登陆使用的是匿名方式链接登陆")

# 3、客户端和服务器进行各种文件传输和信息查询操作
try:
    # 更改当前目录到指定目录
    f.cwd(DIR)
except Exception as e:
    print(e)
    exit()
print("匿名用户更改文件夹新位置{0}".format(DIR))
try:
    '''
    从FTP服务器上下载文件
    第一个参数是FTP命令
    第二个参数是回调函数
    此函数的意思是，执行RETR命令，下载文件到本地后，运行回调函数
    '''
    f.retrbinary('RETR{0}'.format(FILE), open(FILE, 'wb').write)
except Exception as e:
    print(e)
    exit()

# 4、客户端从远程FTP服务器推出，结束传输
f.quit()