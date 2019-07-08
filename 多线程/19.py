# 多进程Process实例对象
import multiprocessing
from time import sleep, ctime

def clock(interval):
    while True:
        print(" The time is %s"%ctime())
        sleep(interval)
if __name__ == "__main__":
    # 子进程调用形式与子线程方式相同
    p = multiprocessing.Process(target=clock, args=(5, ))# 带有元祖参数形式，（5， ）格式
    p.start()
    while True:
        print("sleeping......")
        sleep(1)