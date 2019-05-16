    # 返回函数
'''
- 函数可以返回具体的值
- 也可以返回一个函数作为结果
'''

#定义一个普通函数
def myF(a):
    print('In myF')
    return None
a = myF(8)
print(a)
#函数作为返回值返回，被返回的函数在函数体内定义
def myF2():
    def myF3():
        print('In myF3')
        return 3
    return myF3
# 使用上面定义
# 调用myF2,返回一个函数myF3,赋值给f3
f3 = myF2()
print(type(f3))
print(f3)
f3()
print(f3())
# 复杂一点的返回函数例子
'''
-args:参数列表
-myF4定义函数，返回内部定义的函数myF5
-myF5使用外部变量，这个变量是myF4的参数
'''
def myF4(*args):
    def myF5():
        rst = 0
        for n in args:
            rst += n
        return rst
    return myF5
f5 = myF4(1,2,3,4,5,6,7,8,9,0)
print(f5())
f6 = myF4(10,20,30,40,50)
print(f6())

# 闭包
'''
-当一个函数在内部定义函数，并且内部的函数应用外部函数的参数或者局部变量，当内部函数
    被当做返回值的时候，相关参数和变量保存在返回的函数中，这种结果，叫闭包
-上面定义的myF4是一个标准闭包结构
'''
# 闭包常见问题 举例1
def count():
    # 定义列表，列表里存放的是定义的函数
    fs = []
    for i in range(1,4):
        # 定义了一个函数f，同时函数f是一个闭包结构
        def f():
            return i * i
        fs.append(f)
    return fs
f7,f8,f9 = count()
print(f7())
print(f8())
print(f9())
# 出现的问题：
'''
- 造成上述状况的原因是,返回函数引用了变量i， i并非立即执行，而是等到三个函数都
    返回的时候才统一使用，此时i已经变成了3，最终调用的时候，都返回的是 3*3
- 此问题描述成：返回闭包时，返回函数不能引用任何循环变量
- 解决方案： 再创建一个函数，用该函数的参数绑定循环变量的当前值，无论该循环变量
    以后如何改变，已经绑定的函数参数值不再改变
'''
#解决上述闭包问题的方案如下
def count2():
    # 创建一个新函数，用来绑定循环变量的当前的值i
    def f(i):
        # 创建函数来接受变量操作之后的值，并返回该值
        def g():
            return i * i
        return g
    fs2 = []
    for i in range(1,4):
        fs2.append(f(i))
    return fs2
f10,f11,f12 = count2()
print(f10())
print(f11())
print(f12())