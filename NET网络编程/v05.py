# TCP编程客户端程序
import socket

# 客户端函数
def tcp_cli():
    # 1、建立通信socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、链接对方服务器，请求跟对方建立通路
    addr = ('127.0.0.1', 8998)
    sock.connect(addr)
    # 3、发送内容到对方服务器
    msg = "客户通过ICP请求建立通信"
    # 发送内容字符串（str）格式，需要编码为bytes格式.encode(),服务器才能读取
    sock.send(msg.encode())
    # 4、接受对方的反馈
    rst = sock.recv(500)
    # 接受到反馈内容为bytes格式，需要解码为字符串（str）格式.decode()，客户端才能读取
    print(rst.decode())
    # 5、关闭链接通路
    sock.close()

# 客户端启动函数
if __name__ == '__main__':
    tcp_cli()