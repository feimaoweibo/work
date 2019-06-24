# LOG - 搭配装饰器使用
#习题2，在函数执行前打印日志信息
import logging
log_format = "%(asctime)s----%(levelname)s-----%(message)s"
logging.basicConfig(format=log_format, filename="习题2.log")
def log(func):
    def wrapper(*args, **kwargs):
        logging.error("这是习题2---error级别的日志")
        return func(*args, *kwargs)
    return wrapper
@log
def test():
    print("函数执行前面，显示日志信息")
test()

