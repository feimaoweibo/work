# 服务器端配置文件
class ServerContent:
    ip = '127.0.0.1'
    port = 9876
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
    # 指定路由功能的函数
    def reRoute(self):
        uri = self.headInfo.get('uri') # 获取URI资源名
        # 如果uri 是b'/'
        if uri == b'/':
            self.sendRsp(r'./webapp/hello.html')
            return None
        # 如果uri 是b'/favicon.ico'图标
        if uri == b'/favicon.ico':
            self.sendStaticTco(r'./static/fav.jfif')
            return None
        # 不然请求访问的资源名不存在
        self.sendRsp(r'./webapp/404.html')
    # 发送页面图标函数
    def sendStaticTco(self, fp):
        with open(fp, mode='rb') as f:
            ico = f.read()
            self.__sendRspALL(ico)

    # 处理请求的http协议函数
    def headHandler(self):
        self.headInfo = dict() # headInfo内容是个字典格式的http协议
        # 两个下划线开头的函数：用于对象的数据封装，以此命名的属性或者方法为类的私有属性或者私有方法。
        '''
        "单下划线" 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；
        "双下划线" 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。
        '''
        tmpHead = self.__getAllLine() # 获取所有行的内容，赋值给tmpHead
        for line in tmpHead:
            if b':' in line: # 如果b':'格式的分号，在所有行里面，则该行为http协议的首部行
                # str.split(b':')函数指定符号进行分割，放入Dick字典
                infos = line.split(b':')
                # 采用Dick字典键值对格式赋值
                self.headInfo[infos[0]] = infos[1]
            else:
                # 则按str.split(b' ')格式的空格，分割放入dick字典
                infos = line.split(b' ')
                # 自定义http协议的请求行的三部分内容，分别为method方法、URI资源名、protocal版本
                self.headInfo['protocal'] = infos[2]
                self.headInfo['method'] = infos[0]
                self.headInfo['uri'] = infos[1]
    # 发送反馈信息函数
    def sendRsp(self):
        '''
        想返回一个静态页面，可以考虑把静态页面文件读入，作为str类型，然后作为一个长字符串返回
        '''
        fp = r'.\webapp\hello.html'
        with open(fp, mode='r', encoding='utf-8') as f:
            data = f.read()
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
