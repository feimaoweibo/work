# concurrent.futures异步map函数案例1、
import time
import os, datetime
from concurrent import futures

data = ['1', '2']
def wait_on(argument):
    print(argument)
    time.sleep(2)
    return 'ok!'
# 创建线程池，最大允许运行2个核心
ex = futures.ThreadPoolExecutor(max_workers=2)
# 往线程池加入map()函数，异步执行（同时打印1，2），间隔2秒后返回结果字符串
for i in ex.map(wait_on, data):
    print(i)