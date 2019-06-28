# 可以继承threading.Thread类
import threading
import time

# 1、类需要继承自 threading.Thread
class MyThread(threading.Thread):
    def __init__(self, args):
        super(MyThread, self).__init__()
        self.arg = args
    # 2、必须重写run函数，run函数代表真正执行的功能
    def run(self):
        time.sleep(2)
        print("The args for this class is {0}".format(self.arg))
for i in range(5):
    t = MyThread(i)
    t.start()
    t.join()
print("Main thread is done!!!!!!!")