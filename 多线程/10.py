# 子线程类继承 西方工业化风格
import threading
from time import sleep, ctime
loop = [4,2]
class ThreadFunc:
    def __init__(self, name):
        self.name = name
    def loop(self, nloop, nsec):
        '''
        :param nloop: loop函数的名称
        :param nsec: 系统休眠时间
        :return:
        '''
        print("start loop ", nloop, "at", ctime())
        sleep(nsec)
        print("done loop ", nloop, "at", ctime())
def main():
    print("Starting At:",ctime())
    # ThreadFunc("loop").loop 跟一下两个式子相等：
    # t = ThreadFunc("loop")
    # t.loop
    # 以下t1 和  t2的定义方式相等
    t = ThreadFunc("loop")
    t1 = threading.Thread(target=t.loop, args=("loop1", 4))
    # 下面t2为西方人士写法
    t2 = threading.Thread(target=ThreadFunc("loop").loop, args=("loop2", 2))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("All Done At:",ctime())
if __name__ == "__main__":
    main()


