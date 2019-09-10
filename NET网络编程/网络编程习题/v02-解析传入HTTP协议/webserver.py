# v02-解析传入HTTP协议
'''
- 根据http协议格式，逐行读取信息
- 按行读取后的信息，需要进行拆解
'''
import socket
# 获取协议头函数
def getHttpHeader(skt):
    '''
    得到传入socket的http请求头
    :param skt: 通信的skt
    :return: 解析后的请求头内容，字典形式
    '''
    # 用来存放返回 解析后的请求头内容（字典格式）
    rst = {}
    # 读取某一行，直到读取的行返回空行为止
    line = getLine(skt)
    while line:
        '''
        判断得到行是报头还是首部行，两个操作方法不一样，算法是：
        1、利用str.split(":")作为分隔符，分割字符串
        2、如果是首部行，则一定会把字符串分成2个子串
        3、否则就是一个字符串
        '''
        r = line.split(r': ')
        if len(r) == 2:
            rst[r[0]] = r[1]
        else:
            r = line.split(r' ')
            rst['method'] = r[0]
            rst['url'] = r[1]
            rst['version'] = r[2]
        line = getLine(skt)
    return rst

# 获取行内容函数
def getLine(skt):
    '''
    从socket中读取某一行
    :param skt: socket
    :return: 返回读取到一行的str格式内容
    '''
    '''
    前提条件：
    1、http协议传输内容是ascii编码
    2、真正传输的内容是通过网络流传输的
    3、回车换行：b'\r', b'\n', b表示是一个bytes格式
    '''
    # 每次从socket读取一个byte内容
    b1 = skt.recv(1)
    b2 = 0
    # data用来存放读取的的行的内容
    data = b' '
    # 当确定还没有到读到一行最后，即回车换行符号的时候，需要循环
    while b2 != b'\r' and b1 !=b'\n':
        b1 = skt.recv(1)
        data += bytes(b2)
    # decode(编码)，默认编码为utf-8
    return data.strip(b'\r').decode()

# 以下为服务器端代码示例
# 创建一个socket，并带有2个参数的含义
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定地址addr,注意addr的格式为tuple(元祖格式)
sock.bind(('127.0.0.1', 7852))
print("已经绑定端口")
# 监听
sock.listen()
print("已经开始监听")
# 接受一个传进来的socket
skt, addr = sock.accept()
print("已经接收到传入的socket:{0}".format(skt))
# 实际处理请求的内容
http_info = getHttpHeader(skt)
print(http_info)

# 对对方一个反馈
msg = "我已经收到，现在反馈信息给你++++++++"
skt.send(msg.encode())
skt.close()
sock.close()