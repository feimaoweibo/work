'''
Server端流程
 1. 建立socket，socket是负责具体通信的一个实例
 2. 绑定，为创建的socket指派固定的端口和ip地址
 3. 接受对方发送内容
 4. 给对方发送反馈，此步骤为非必须步骤
'''

# socket模块负责socket编程
import socket
# 模拟服务器的函数
def serverFunc():
    # 1、建立socket；socket.AF_INET:使用IPv4协议族； socket.SOCK_DGRAM:使用UDP通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2、绑定IP和port，地址是个tuple类型（ip,port）
    addr = ("127.0.0.1", 7852)
    sock.bind(addr)

    # 3、接受对方发送消息
    '''
    等待方式为死等，没有其他可能性
    recvfrom接受的返回值是一个tuple,前一项表示数据，后一项表示地址
    参数的含义是缓冲区大小：rst = sock.recvfrom(500)
    '''
    data, addr = sock.recvfrom(500)
    print(data)
    print(type(data))
    # 发送过来的数据是bytes格式，必须通过解码才能得到str格式内容
    # decode默认参数是utf-8格式
    text = data.decode()
    print(type(text))
    print(text)

    # 4、给对方返回信息
    rsp = "服务器已经接到你们的访问请求，现在返回给你数据++++++++"
    # 发送的数据，需要编码为bytes格式
    # 默认是utf-8格式
    data = rsp.encode()
    sock.sendto(data, addr)
# 启动函数
if __name__ == "__main__":
    print("Starting Server........")
    serverFunc()
    print("Ending server+++++++++")