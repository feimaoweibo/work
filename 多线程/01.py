'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''
import time
def loop1():
    # ctime()函数：得到当前时间
    print("start loop 1 at :", time.ctime())
    # sleep()函数：睡眠（间隔）多长时间,单位是秒
    time.sleep(4)
    print("end loop 1 at :", time.ctime())
def loop2():
    print("start loop 2 at :", time.ctime())
    time.sleep(2)
    print("end loop 2 at :", time.ctime())
def main():
    print("Starting At: ", time.ctime())
    loop1()
    loop2()
    print("All done At: ", time.ctime())
if __name__ == '__main__':
    main()

