# 文件
'''
- 长久保存信息的一种数据信息集合
- 常用操作
    - 打开关闭（文件一旦打开，需要关闭操作）
    - 读写内容
    - 查找 #open 函数
- open函数 负责打开文件，带有很多参数
    - 第一个参数：r 表示后面字符串内容不需要转义 （必须）
    - 第二个参数：文件的名称和路径 （必须）
    - 第三个参数：mode 表面文件的打开方式
        r：以只读方式打开
        w：以写入方式打开，会覆盖以前的内容
        x：以创建方式打开，如文件已经存在，则报错
        a：以append方式打开，用追加的形式对文件内容进行写入
        b：binary方式，二进制方式写入
        t：文本方式打开
        +：可读写
- 格式为: f = open(r'test01'.txt, 'w')
'''
# 一、案例说明：以写方式打开文件，默认是如果没有文件，则创建
    # f 称之为：文件句柄
f = open(r'test01.txt', 'w')
    # 文件打开后必须关闭
f.close()

# 二、with语句
'''
- with语句使用的技术是一种称为 上下文管理协议的的技术（ContextManagementProtocal)
- 自动判断文件的作用域，自动关闭不再使用已打开的句柄文件
'''
    # 案例1、
with open(r'test02.txt','r') as f:
    # 下面语句块开始对文件f 进行操作
    # 在本模块中不需要在使用close关闭文件f
    pass

    # 案例2、readline() 按行读取
with open(r'test02.txt','r') as f:
    # 按行读取内容
    strline = f.readline()
    # 此结构保证能够完整读取文件直到结束
    while strline:
        print(strline)
        strline = f.readline()
print('--------------'*5)
with open(r'test03.txt', 'r') as f:
    strline1 = f.readline()
    while strline1:
        print(strline1)
        strline1 = f.readline()
print('-------------'*3)

    # 案例3、list（）参数
# list能用打开的文件作为参数，把文件内每一行内容作为一个元素
with open(r'test02.txt', 'r') as f:
    # 以打开的文件f作为参数，创建列表
    l = list(f)
    for i in l:
        print(i)
print('--------'*5)

    # 案例4、 read（）参数
'''
- read 是按字符读取文件内容
- 允许输入参数决定读取几个字符，如果没有指定参数，从当前位置读取到结尾
- 否则，从当前位置读取指定个数字符
'''
with open(r'test02.txt', 'r') as f:
    strChar = f.read(1)
    print(len(strChar))
    print(strChar)

# 习题：使用read（）函数读取文件，每次读取一个，使用循环读完、尽量保持格式
with open(r'test02.txt', 'r') as f:
    sr = f.read()
    while sr:
        print(sr)
        break