# concurrent.futures异步map函数案例2、
from concurrent.futures import ThreadPoolExecutor as Pool
import time
import urllib
from urllib import request

URLS = ['http://www.baidu.com', 'http://www.qq.com', 'http://www.sina.com.cn']

def task(url, timeout=20):
    return request.urlopen(url, timeout=timeout)
# 创建线程池
pool = Pool(max_workers=3)
results = pool.map(task, URLS)
time.sleep(20)
for ret in results:
    print('%s' %(ret.url))

