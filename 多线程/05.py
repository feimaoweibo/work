'''
# 利用time延时函数，生成两个函数
# 利用多线程调用
# 计算总运行时间
# 练习带参数的多线程启动方法
'''
import time
import threading

def loop1(in1):
    print("start loop1 at:", time.ctime())
    print("我是参数：", in1)
    time.sleep(4)
    print("end loop1 at:", time.ctime())
def loop2(in1, in2):
    print("start loop2 at:", time.ctime())
    print("我是参数：", in1, "和参数：", in2)
    time.sleep(2)
    print("end loop2 at:", time.ctime())
def main():
    print("Starting At:", time.ctime())
    # threading.Thread实例
    t1 = threading.Thread(target=loop1, args=("王老大", ))
    t1.start()
    t2 = threading.Thread(target=loop2, args=("王老二", "王老三"))
    t2.start()
    # t.join()等待多线程执行完成后，再继续执行后面的内容
    t1.join()
    t2.join()
    print("All Done At:", time.ctime())
if __name__ == "__main__":
    main()
    while True:
        time.sleep(10)