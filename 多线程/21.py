# 多进程案例 父子关系
import multiprocessing
import os
def info(title):
    print(title)
    print("module name:", __name__)
    # 得到父亲进程ID
    print("parent processID:", os.getppid())
    # 得到自身进程ID
    print("process id:", os.getpid())
def f(name):
    info("function f")
    print("hello", name)
if __name__ == "__main__":
    info("main line")
    p = multiprocessing.Process(target=f, args=('bob', ))
    p.start()
    p.join()