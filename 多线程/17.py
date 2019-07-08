import threading
import time
def func():
    print("I am running......")
    time.sleep(4)
    print("I am  done......")
if __name__ == "__main__":
    # threading.Timer()函数是在指定具体时间后启动多线程的一个功能，这里是6秒以后
    t = threading.Timer(6, func)
    t.start()
    i= 0
    '''
    打印结果是：间隔3秒打印一行内容
    0*******
    1*******
    2*******此时刚好6秒，开始打印线程内容：I AM RUNNING（间隔4秒后，再打线程内容）
    3*******（距离3秒后打印的内容）
    I AM DONE（间隔到第4秒时打印线程内容）
    4*******
    5*******
    --------
    '''
    while True:
        print("{0}************************".format(i))
        time.sleep(3)
        i += 1