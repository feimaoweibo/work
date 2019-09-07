# 改造服务器
'''
Server端流程：
    1、建立socket，socket是负责具体通信的一个实例
    2、绑定，为创建socket指派固定的端口和IP地址
    3、接受对方发送内容
    4、给对方发送反馈，此步骤非必须步骤
'''
import socket

# 模拟服务器函数
def serverFunc():
    # 1、建立socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2、绑定IP地址和端口（port）
    addr = ("127.0.0.1", 7852)
    sock.bind(addr)

    # 3、等待接受客户端发起的请求
    data, addr = sock.recvfrom(500)
    print(data)
    print(type(data))
    # 发送过来的数据是bytes格式，必须通过解码才能得到str格式内容
    # decode默认参数是utf-8格式
    text = data.decode()
    print(type(text))
    print(text)

    # 4、给客户端发送反馈信息
    rsp = "服务器已经收到客户端的请求，现在发送数据给客户端"
    data = rsp.encode()
    sock.sendto(data, addr)

# 服务器启动函数
if __name__ == "__main__":
    import time
    while 1:
        try:
            serverFunc()
        except Exception as e:
            print(e)
        time.sleep(1)