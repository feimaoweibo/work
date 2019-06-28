'''
#利用time延时函数，生成两个函数
# 利用多线程调用
# 计算总运行时间
# 练习带参数的多线程启动方法
'''
import time
# 导入多线程处理包
import threading

def loop1(in1):
    print("start loop1 at:", time.ctime())
    print("我是参数：", in1)
    time.sleep(4)
    print("end loop1 at:", time.ctime())
def loop2(in1, in2):
    print("start loop2 at:", time.ctime())
    print("我是参数： ", in1, "和参数：", in2)
    time.sleep(2)
    print("end loop2 at:", time.ctime())
def main():
    print("Starting At:", time.ctime())
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1, args=("王老大", ))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("王老二", "王老三"))
    t2.start()
    print("All Done At:", time.ctime())

if __name__ == "__main__":
    main()
    while True:
        time.ctime(10)