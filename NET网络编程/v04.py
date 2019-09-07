# FTP编程服务器端程序
import socket

def tcp_srv():
    # 1、建立socket负责具体通信，这个socket其实只负责接受对方的请求，真正通信的是链接后重新建立的socket
    # 此次.AF_INET:表示通信IPv4地址; .SOCK_STRAM:表示使用TCP方式通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、绑定端口和地址
    addr = ('127.0.0.1', 8998)
    sock.bind(addr)
    # 3、监听接入的访问socket
    sock.listen()

    while True:
        # 4、接受访问的socket,可以理解接受访问即建立了一个通信的链接通路
        # accept返回的元组（tuple）第一个元素赋值给skt,第二个赋值给addr
        skt, addr = sock.accept()
        # 5、接受对方发送内容，利用接收到的socket接受内容
        msg = skt.recv(500)
        # 接受的是bytes格式内容，需要解码为字符串（str）格式内容
        msg = msg.decode()
        rst = "服务器已经接受请求，显示发送内容：{0}".format(msg, addr)
        print(rst)
        # 6、如果有必要，给对方发送反馈信息
        skt.send(rst.encode())
        # 7、关闭链接通路
        skt.close()
# 服务器启动函数
if __name__ == '__main__':
    print("Starting TCP server---------")
    tcp_srv()
    print("Ending TCP sever++++++++")