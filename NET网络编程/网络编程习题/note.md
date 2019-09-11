# HTTP项目实战
    - 深入理解HTTP协议
    - 模拟后台服务程序基本流程和大致框架
    - 每一个步骤一个文件夹
    - 推荐图书：《图解HTTP协议》、《图解TCP/IP协议》
# v01-验证技术
    - 验证socket-tcp技术，看能否走通流程
    - 目的：使用浏览器发送信息，访问地址
# v02-解析传入HTTP协议
    - 根据http协议格式，逐行读取信息
    - 按行读取后的信息，需要进行拆解
# v03-http协议封装返回内容
    - 返回头： "HTTP/1.1 200 OK\r\n"
    - 首部行： 
        - "Content-Length: xxx\r\n"
        - "Date: 20190911\r\n"
    - 空行："\r\n"
    - 返回内容： "I love beijing tulingxueyuan"
# -v04-面向对象重构
    - 两个对象：
        一个负责监听接受传入socket,称为WebServer
        一个负责通讯，称为SocketHandler