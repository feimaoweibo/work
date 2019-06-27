# 多线程，传参数
'''
#利用time延时函数，生成两个函数
# 利用多线程调用
# 计算总运行时间
# 练习带参数的多线程启动方法
'''
import time
import _thread as thread

def loop1(in1):
    print("start loop1 at:", time.ctime())
    print("我是参数 ", in1)
    time.sleep(4)
    print("end loop1 at:", time.ctime())
def loop2(in1, in2):
    print("start loop2 at:", time.ctime())
    print("我是参数 ", in1, "和参数 ", in2)
    time.sleep(2)
    print("end loop2 at:", time.ctime())
def main():
    print("Starting at ：", time.ctime())
    '''
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thead
    # 参数两个，一个是需要运行的函数名，第二是函数的参数为元祖格式，为空则使用空元祖
    # 注意：如果函数带只有一个参数，则需要参数后加上：一个逗号与空格
    '''
    thread.start_new_thread(loop1,("王老大", ))
    thread.start_new_thread(loop2,("王老二", "王老三"))
    print("All Done at:", time.ctime())

if __name__ == '__main__':
    main()
    '''
    一定要有while语句
    因为启动多线程后本程序就作为主线程存在
    如果主线程执行完毕，则子线程可能也需要终止
    '''
    while True:
        time.sleep(10)
