#!user/bin/env python3
# -*- coding: gbk -*-
#根据不同的函数，使用装饰器来传入不同的日志信息
import logging
log_format = "%(asctime)s------ %(levelname)s ----%(message)s"
logging.basicConfig(format=log_format, filename="习题3.log")
def log(zhi):
    def lianxi(func):
        def wrapper(*args, **kwargs):
            logging.warning(zhi)
            return func(*args, **kwargs)
        return wrapper
    return lianxi

@log("函数lstest的变量")
def lstest():
    print("传入参数1的函数结果")
@log("函数lstest2的变量")
def lstest2():
    print("传入参数2的函数结果")
lstest()
lstest2()