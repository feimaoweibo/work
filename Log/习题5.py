# 用logging的四大组件来实现日志的功能
'''
-打应出函数执行的时间，日志的等级，日志的消息
-用装饰器
-不同的日志，要记录不同等级的日志消息
'''
import logging
# 实例化一个logger
logger = logging.getLogger("mylogger")
# 设置日志级别
logger.setLevel(logging.DEBUG)
# 根据日志不同分类，添加对应的处理器：handler
de_handler = logging.FileHandler("习题5DEBUG日志.log")
de_handler.setLevel(logging.DEBUG)
de_handler.setFormatter(logging.Formatter("%(asctime)s-----%(levelname)s-----%(message)s"))

er_handler = logging.FileHandler("习题5ERROR日志.log")
er_handler.setLevel(logging.ERROR)
er_handler.setFormatter(logging.Formatter("%(asctime)s-----%(levelname)s-----%(message)s"))
# 绑定处理器
logger.addHandler(de_handler)
logger.addHandler(er_handler)
'''
logger.warning('案例2----warning message')
logger.error('案例2----error message')
'''
def log(func):
    def wrapper(*arg, **kwargs):
        logger.debug("这是习题5结合装饰器记录debug级别的日志")
        logger.error("这是习题5结合装饰器记录error级别的日志")
        return func(*arg, **kwargs)
    return wrapper

def loghigher(text):
    def dec(func):
        def wrapper(*args, **kwargs):
            logger.debug(text)
            logger.error(text)
            return func(*args, **kwargs)
        return wrapper
    return dec

@log
def doFunc():
    print("这是习题5装饰器日志使用方法")
doFunc()

@loghigher("带参数的debug级别日志")
def warn():
    print("debug级别日志信息")
@loghigher("带参数的error级别的日志")
def err():
    print("error级别日志信息")
warn()
err()
