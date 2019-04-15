# 如果是多种error的情况
# 需要把越具体的错误，越往前放
# 在异常类继承关系中，越是子类的异常，越要往前放，
# 越是父亲类的异常，越要往后放
# 在处理异常的时候，一旦拦截到某一个异常，则不在继续往下查看，直接进行下一个代码，即有finally则执行finally语句块，否则就执行下一个大的语句
# 所有异常都是继承自Exception，任何异常都会拦截住。而且，下面这句话一定是最后一个exception
try:
    num1 = int(input('请输入数字：'))
    rst = 1000 / num1
    print('计算结果是：{0}'.format(rst))
except ZeroDivisionError as e:
    print('不能输入数字0')

except ValueError as e:
    print('不能包含有字母')
# 所有异常都是继承自Exception，任何异常都会拦截住。而且，下面这句话一定是最后一个exception
except Exception as e:
    print('我也不知道的错误类型')

finally:
    print('自动执行内容')
