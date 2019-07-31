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
        a, b = b, a+b#把原始b的值赋值给a, 把原始a+b的值赋值给b
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