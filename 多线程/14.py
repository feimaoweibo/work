import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def fun_1():
    print("fun_1 starting......")
    lock_1.acquire()
    print("fun_1 申请了 lock_1----")
    time.sleep(2)
    print("fun_1 等待 lock_2----")
    lock_2.acquire()
    print("fun_1 申请了 lock_2----")

    lock_2.release()
    print("fun_1 释放了 lock_2----")
    lock_1.release()
    print("fun_1 释放了 lock_1----")

    print("fun_1 done。。。。")
def fun_2():
    print("fun_2 starting.......")
    lock_2.acquire()
    print("fun_2 申请了 lock_2====")
    time.sleep(4)
    print("fun_2 等待 lock_1====")
    lock_1.acquire()
    print("fun_2 申请了 lock_1====")

    lock_1.release()
    print("fun_2 释放了 lock_1")
    lock_2.release()
    print("fun_2 释放了 lock_2")

    print("fun_2 done========")

if __name__ == "__main__":
    print("主程序启动++++++++++")
    t1 = threading.Thread(target=fun_1, args=())
    t2 = threading.Thread(target=fun_2, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("主程序结束============")