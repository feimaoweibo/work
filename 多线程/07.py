# 守护线程案例，能否有效果与环境有关
import time
import threading

def fun():
    print("start fun")
    time.sleep(2)
    print("end fun")
print("Main thread start")
t1 = threading.Thread(target=fun, args=())
# 启动守护线程的方法，必须在t.start（）之前设置，否则无效
t1.setDaemon(True)
t1.start()
time.sleep(1)
print("Main thread end")