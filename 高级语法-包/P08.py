# raise 案例1
try:
    print('打印第一条内容11111111')
    print('打印第二条内容22222222')
    # 手动引发一个异常
    # 注意语法  raise ErrorClassName
    raise ValueError
except NameError as e:
    print('名字错误')
except ValueError as e:
    print('用户手动引发一个异常了')
except Exception as e:
    print('异常触发了')

print('------11111111---------'*5)

# raise 案例2 自定义异常
# 注意：自定义异常必须是系统异常的子类
class zidingyiValueError(ValueError):
    pass
try:
    print('打印内容333333333')
    print('打印内容444444444')
    raise zidingyiValueError
    print('引发自定义异常后，该内容不得打印了')
except NameError as e:
    print('名字错误')
except ValueError as e:
    print('用户引发自定义异常')
except Exception as e:
    print('异常种类')