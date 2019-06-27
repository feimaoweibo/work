'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''
import time
import _thread as thread
def loop1():
    print("start loop1 at:", time.ctime())
    time.sleep(4)
    print("end loop1 at:", time.ctime())
def loop2():
    print("start loop2 at: ", time.ctime())
    time.sleep(2)
    print("end loop2 at: ", time.ctime())
def main():
    print("Starting At:", time.ctime())
    '''
    启动多线程的意思：用多线程去执行某个函数
        启动多线程函数为：start_new_thread(func, (参数))
            参数两个，一个是需要运行的函数名，第二是函数的参数为元祖格式，为空则使用空元祖
            注意：如果函数带只有一个参数，则需要参数后加上：一个逗号与空格
    '''
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())
    print("All Done At:", time.ctime())
if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)