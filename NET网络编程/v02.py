'''
Client端流程
    1. 建立通信的socket
    2. 发送内容到指定服务器
    3. 接受服务器给定的反馈内容
'''

import socket
# 模拟客户端通信函数
def clientFunc():
    # 1、建立通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2、发送内容到服务器
    text = "客户端发起访问申请，现在发送请求ing........"
    # 发送的数据必须是bytes格式，需要先编码
    data = text.encode()
    # 开始发送数据
    sock.sendto(data, ("127.0.0.1", 7852))
    # 3、等待返回数据
    '''
    等待方式为死等，没有其他可能性
    recvfrom接受的返回值是一个tuple,前一项表示数据，后一项表示地址
    参数的含义是缓冲区大小：rst = sock.recvfrom(500)
    '''
    data, addr = sock.recvfrom(200)
    # 返回的数据格式为bytes,需要解码为str数据格式内容
    data = data.decode()
    print(data)

# 客户端启动函数
if __name__ == "__main__":
    clientFunc()