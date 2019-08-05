# 一、协程
'''
-参考资料
http://python.jobbole.com/86481/
http://python.jobbole.com/87310/
https://segmentfault.com/a/1190000009781688
'''

# 二、迭代器
'''
可迭代（Iterable）:直接作用于for循环的变量
迭代器（Iterator）:不但可以作用于for循环，还可以被next调用
    list是典型的可迭代对象，但不是迭代器
通过isinstance()判断
iterable 于 iterator 可以通过 iter()函数转换
'''
#可迭代变量举例
l = [i for i in range(10)]
for idx in l:
    print(idx)
#迭代器变量举例
for i in range(5):
    print(i)
#isinstance()举例
l1 = [1,2,3,4,5]
from collections import Iterable, Iterator
print(isinstance(l1, Iterable))# 判断某个变量是否是一个可迭代实例
print(isinstance(l1, Iterator))# 判断是否是迭代器
#iter（）函数举例
s = 'i love wangxiaojing'
print(isinstance(s, Iterable))
print(isinstance(s, Iterator))#值为False，不是迭代器
s_iter = iter(s) #通过iter()函数，把可迭代实例转换成迭代器实例
print(isinstance(s_iter, Iterable))
print(isinstance(s_iter, Iterator))#值为True,转换为迭代器
print("------------分割线----二----迭代器---------------")

# 三、生成器
'''
generator:含义为一边循环一边计算下一个元素的的机制或算法
需要满足三个条件：
    每次调用都生产出for循环需要的下一个元素
    如果达到最后一个元素后，报出StopIteration异常
    可以被next函数调用
如何生成一个生成器：
    直接使用
    如果函数中包含yield，则这个函数就叫生成器
    next()调用函数，遇到yield则返回
'''
#直接使用生成器
L = [x*x for x in range(5)]#放在中括号中是列表生成器
g = (x*x for x in range(5))#放在括号中是      生成器
print(type(L))
print(type(g))
#生成器函数案例
def odd():
    print('Step 1')
    yield 1 #yield负责返回
    print('Step 2')
    yield 2
    print('Step 3')
    yield 3
g = odd()
one = next(g)
print(one)
two = next(g)
print(two)
three = next(g)
print(three)
#for循环调用生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b # 把原始b的值赋值给a, 把原始a+b的值赋值给b
        n += 1
    return 'Done'
fib(5)
print('**************')
# 斐波那契额数列的生成器写法
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n +=1
    # 需要注意，爆出异常是的返回值是return的返回值
    return 'Done'
'''
f = fib1(5)
for i in range(6):
    rst = next(f)
    print(rst)
print('--------------')
'''
# 在for循环中使用生成器
'''
生成器的典型用法是在for中使用
比较常用的典型生成器就是range
'''
f1 = fib1(10)
for i in f1:
    print(i)

# 四、协程定义
'''
-历史历程
    3.4引入协程，用yield实现
    3.5引入协程语法
    实现的协程比较好的包有asyncio, tornado, gevent
-定义：协程 是为非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置暂停或开始执行程序”。
-从技术角度讲，协程就是一个你可以暂停执行的函数，或者干脆把协程理解成生成器
-协程的实现：
    yield返回
    send调用
    代码案例v01
-协程的四个状态
    inspect.getgeneratorstate(…) 函数确定，该函数会返回下述字符串中的一个：
    GEN_CREATED：等待开始执行
    GEN_RUNNING：解释器正在执行
    GEN_SUSPENED：在yield表达式处暂停
    GEN_CLOSED：执行结束
    next预激（prime)
    代码案例v2
-协程终止
    协程中未处理的异常会向上冒泡，传给 next 函数或 send 方法的调用方（即触发协程的对象）
    终止协程的一种方式：发送某个哨符值，让协程退出。内置的 None 和Ellipsis 等常量经常用作哨符值==。
-异常
    客户端代码可以在生成器对象上调用两个方法
        generator.throw(Exctpiton):
            指使生成器在暂停的 yield 表达式处抛出指定的异常。如果生成器处理了
            抛出的异常，代码会向前执行到下一个 yield 表达式，而产出的值会成为
            调用 generator.throw方法得到的返回值。如果生成器没有处理抛出的异常
            ，异常会向上冒泡，传到调用方的上下文中。
        generator.close():
            指使生成器在暂停的 yield 表达式处抛出 GeneratorExit 异常。
            如果生成器没有处理这个异常，或者抛出了 StopIteration 异常（通常是指运行到结尾），
            调用方不会报错。如果收到 GeneratorExit 异常，生成器一定不能产出值，否则解释器会
            抛出RuntimeError 异常。生成器抛出的其他异常会向上冒泡，传给调用方。
    案例v03-1
-yield from
    调用协程为了得到返回值，协程必须正常终止
    生成器正常终止会发出StopIteration异常，异常对象的vlaue属性保存返回值
    yield from从内部捕获StopIteration异常，并且把StopIteration异常value属性值作为yield from表达式的返回值
    案例v03
    委派生成器
        包含yield from表达式的生成器函数
        委派生成器在yield from表达式处暂停，调用方可以直接把数据发给自生成器
        子生成器在把产出的值发给调用方
        自生成器在最后，解释器会抛出StopIteration，并且把返回值赋加到异常对象上
        案例v04
'''
# 四.1 协程 asyncio 包
'''
python3.4开始引入的标准库,内置了对异步i/o的支持
asyncio本身是一个消息循环,
步骤
    创建消息循环
    把协程导入
    关闭
案例v05
案例v06-两个tasks
案例v07-得到多个网站
'''

# 四.2 协程 asynci and await 包
'''
为了更好的表示异步i/o
python3.5 开始引入
让coroutine代码更简洁
使用上,可以简单进行替换
    可以把 @asyncio.coroutine 替换成async
    yield from 替换成await
案例v08, 把案例06直接替换
'''

# 四.3 协程 aiohttp包
'''
介绍
    asyncio实现单线程并发IO,在客户端用处不大
    在服务器端可以asyncio+coroutine配合,因为http是io操作
    asyncio实现了TCP,UIDP,SSL等协议
    aiohttp是给予asyncio实现的HTTP框架
    pip install aiohttp
    案例09  缺少安装模块
'''

# 四.4 协程concurrent.futures 包
