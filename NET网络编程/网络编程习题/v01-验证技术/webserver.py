import socket
# 创建一个socket编程的过程，理解2个参数的含义
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 注意地址的格式是tuple（元组)内容，包含2个元素
sock.bind(("127.0.0.1",10001))
print("已经绑定地址和端口........")
# 监听有发送请求
sock.listen()
print("正在监听中，等待访问者发送请求++++++")
# 接收一个传进来的socket
print("准备接受socket传入的请求数据")
skt, addr = sock.accept()
print("已经接收到传入socket：{0}".format(skt))
# 读取传入的信息，注意，读取信息的长度一定要小于实际消息的长度
msg = skt.recv(10)
print(type(msg))
# 由于接收到的信息，是bytes格式，需要解码即.decode()
print(msg.decode())
# 给对方一个反馈信息,同时该信息需要编码为bytes格式才能发送
msg = "已经收到客户端的请求，现在给你反馈信息+++++++++++++++++"
skt.send(msg.encode())

# 关闭skt请求
skt.close()
# 关闭sock请求
sock.close()

