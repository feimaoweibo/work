def hello():
    print('Hello World')
hello()
f = hello
f()
# f 和 hello 是一个函数
print(id(f))
print(id(hello))

    # 装饰器(Decrator)
'''
-在不改动函数代码的基础上无限制扩展函数功能的一种机制，
    本质上讲，装饰器是一个返回函数的高阶函数
-装饰器的使用： 使用@语法， 即在每次要扩展到函数定义前使用@+函数名
'''

    # 装饰器案例1、
# 对hello函数进行功能扩展，每次执行hello打印前打印当前时间
import time
def printTime(f):
    '''
    *args 表示将关键字参数打包成tuple（元组格式）给函数体调用，形如：（1,2,3）；
        例子：
            def function(x, y, *args):
                print(x, y, args)
            function(1, 2, 3, 4, 5)
            输出结果：1，2，（3,4,5）
    *kwargs表示将关键字参数打包成dict（字典格式）给函数体调用，形容：{'a':1 ；'b':2 ；'c':3}
        例子：
            def function(**kwargs):
                print(kwargs)
            function(a=1, b=2, c=3)
            输出结果：{'a':1 ；'b':2 ；'c':3}
    -注意点：参数arg、*args、**kwargs三个参数的位置必须是一定的。必须是(arg,*args,**kwargs)这个顺序，否则程序会报错
        例子：
            def function(arg,*args,**kwargs):
                print(arg,args,kwargs)
            function(6,7,8,9,a=1, b=2, c=3)
            输出结果：6 （7,8,9） {'a':1；'b':2； 'c':3}
    '''
    def wraper(*args,**kwargs):
        print('当前时间：',time.ctime())
        return f(*args,**kwargs)
    return wraper
@printTime
def hello():
    print('HELLO WORLD')
hello()

    # 装饰器案例2、
'''
饰器的好处是，一点定义，则可以装饰任意函数
一旦被其装饰，则则把装饰器的功能直接添加到定义函数的功能上
'''
@printTime
def hello2():
    print('装饰器提供了可变参数*args')
    print('装饰器提供了关键字参数**kwargs')
hello2()

    # 装饰器案例 3、手动执行装饰器
'''
上面对函数的装饰使用了系统定义的语法糖
下面开始手动执行下装饰器
'''
def hello3():
    print('我是手动执行的')
hello3()
hello3 = printTime(hello3) #把hello3函数作为参数传入printTime（），执行函数wraper（）,输出结果为2个，第一结果：print当前时间；第二结果为返回函数hello3，因此printTime()最终结果为返回函数wraper(),再赋值给hello3
hello3() #新的hello3调用函数，输出结果：1、当前时间：     2、我是手动执行的
print('-----分割线下'*5)
f = printTime(hello3)
f()