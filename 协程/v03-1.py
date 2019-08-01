# 异常案例
class DemoException(Exception):
    '''
    custom exception
    '''
    pass

def handle_exception():
    print('-> start')
    while True:
        try:
            x = yield
        except DemoException:
            print('-> run demo exception')
        else:
            print('-> recived x:', x)
    raise RuntimeError('this line should never run')

he = handle_exception()
next(he)
he.send(10) # 值为 recived x: 10
he.send(20) # 值位 recived x: 20
# 使用generator.throw(Exception)函数，指使生成器在暂停的yield表达式处抛出指定的异常
he.throw(DemoException) # 值为 run demo exception
he.send(40) # 值为 recived x: 40
# 使用generator.close()函数，指使生成器在暂停的yield表达式处抛出generatorExit异常
he.close()