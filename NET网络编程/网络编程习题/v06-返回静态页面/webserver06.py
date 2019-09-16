# 服务器端配置文件
class ServerContent:
    ip = '127.0.0.1'
    port = 9999
    head_protocal = 'HTTP/1.1'
    head_code_200 = '200'
    head_status_OK = 'OK'

    head_content_length = 'Content-Length:'
    head_content_type = 'Content-type:'
    content_type_html = 'text/html'

    blank_line = ''

import socket
import threading

# 负责通信socket
class SocketHandler:
    def __init__(self, sock):
        self.sock = sock
        # 放置Http请求的头部信息
        self.headInfo = set()
    # 启动函数
    def startHandler(self):
        '''
        处理传入请求的做两件事情
        1、解析http协议
        2、返回return内容
        :return:
        '''
        self.headHandler() # 处理请求http协议
        self.sendRsp() # 发送反馈信息
        return None
    # 处理请求的http协议函数
    def headHandler(self):
        # 两个下划线开头的函数：用于对象的数据封装，以此命名的属性或者方法为类的私有属性或者私有方法。
        '''
        "单下划线" 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；
        "双下划线" 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。
        '''
        self.headInfo = self.__getAllLine() # 获取所有行的内容，赋值给headInfo
        print(self.headInfo)
        return None
    # 发送反馈信息函数
    def sendRsp(self):
        data = "HELLO WORLD"
        self.__sendRspALL(data)
        return None
########################################
    # 读取行内容函数
    def __getLine(self):
        b1 = self.sock.recv(1)
        b2 = 0
        data = b'' # bytes格式数据
        # b2b1不等与回车、换行时，while循环永远执行
        while b2 != b'\r' and b1 != b'\n':
            b2 = b1
            b1 = self.sock.recv(1)
            data += bytes(b2)
        return data.strip(b'\r') # str.strip()就是把字符串(str)的头和尾的空格，以及位于头尾的\n \t之类给删掉。
    # 获取所有行的内容函数
    def __getAllLine(self):
        data = b''
        dataList = list() # 所有内容放入集合列表里
        data = b''
        while True:
            data = self.__getLine() # 单行内容，赋值给data
            if data:
                dataList.append(data) # 如果是单行内容，就把该内容通过append（）函数加入所有行内容的集合列表里
            else:
                return dataList
        return None
    # 发送反馈信息的函数
    def __sendRspLine(self, data):
        data += '\r\n' # 反馈的信息，为data+ '\r\n'(回车加换行)
        self.sock.send(data.encode())
        return None
    # 发送接受请求后的所有报文头信息，标准格式信息如下：
    def __sendRspALL(self, data):
        self.__sendRspLine('HTTP/1.1 200 0K')
        strRsp = 'Content-Length: '
        strRsp += str(len(data))
        self.__sendRspLine(strRsp)
        self.__sendRspLine('Content-Type: text/html')
        self.__sendRspLine('')
        self.__sendRspLine(data)

# 接受传入请求socket
class WebServer():
    # 初始化对象
    def __init__(self, ip=ServerContent.ip, port=ServerContent.port):
        self.ip = ip
        self.port = port
        # 通信采用tcp协议，IP4地址
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定地址和端口
        self.sock.bind((self.ip, self.port))
        # 监听传入socket请求
        self.sock.listen(1)
        print("WebServer is started ------------------")
    # 启动函数
    def start(self):
        '''
        服务器程序一共永久性不间断提供服务
        :return:
        '''
        while True:
            skt, addr = self.sock.accept()
            if skt:
                print("Received a socket {0} from {1}......".format(skt.getpeername(), addr))
                # sokHeadler负责具体通信
                sockHandler = SocketHandler(skt)
                # 多线程引入
                thr = threading.Thread(target=sockHandler.startHandler, args=( )) # 使用类里面的函数名
                thr.setDaemon(True)
                thr.start()
                thr.join()
                skt.close()
                print("Socket {0} handling is done.........".format(addr))

if __name__ == "__main__":
    ws = WebServer()
    ws.start()
