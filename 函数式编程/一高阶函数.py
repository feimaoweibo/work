# 高阶函数---把函数作为参数使用的函数

    # 变量可以赋值
a = 100
b = a

    # 函数名称就是一个变量
def funA():
    print('in funA')
funB = funA
funB()

# 以上代码得出结论：
'''
- 函数名称是变量
- funB 和 funA只是名称不一样而已
- 既然函数名称是变量，则应该可以被当做参数传入另一个函数
'''

    # 高阶函数举例1
def funA(n): # funA是普通函数，返回一个传入数字的100倍数字
    return n * 100
def funB(n): # 再写一个函数，把传入参数乘以300倍
    return funA(n) * 3 # 最终是想返回300n
print(funB(9))

# 写一个高阶函数
def funC(n,f):
    #假定函数是把n扩大100倍
    return f(n) * 3
# 比较funC和funB, 显然funC的写法要优于funB
print (funC(9,funA))

# 变更需求，把N 放大三十倍，此时funB则无法实现需求
def funD(n):
    return n * 30
print(funC(9,funD))

    # 系统高阶函数-map
'''
- 原意就是映射，即把集合或者列表的元素，每一个元素都按照一定规则进行操作，生成一个新的列表或者集合
- map函数是系统提供的具有映射功能的函数，返回值是一个迭代对象
'''

# 有一个列表，相对列表里的每一个元素乘以10，并得到新的列表
l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i * 10)
print(l2)

# 利用map高阶函数实现上诉功能
def mFun(m1):
    return m1 * 10
l3 = map(mFun,l1)
for i in l3:
    print(i)
l4 = [i for i in l3]
print (l4)

    # 系统高阶函数--- reduce
'''
- 原意是归并，缩减
- 把一个可迭代对象最后归并成一个结果
- 对于作为参数的函数要求：必须有两个参数，必须有返回结果
- reduce（[1,2,3,4,5]）== f(f(f(f(1,2),3),4,),5)
- reduce 需要导入functools包
'''
from functools import reduce
# 定义一个操作函数，返回结果为元素相加
def myAdd(x,y):
    return x + y
# 对于列表[1,2,3,4,5,6]执行myAdd的reduce操作
rst = reduce(myAdd,[1,2,3,4,5,6])
print (rst)

    # 系统高阶函数---filter
'''
- 过滤函数： 对一组数据进行过滤，符合条件的数据会生成一个新的列表并返回
- 跟map相比较：
    - 相同：都对列表的每一个元素逐一进行操作
    - 不同：
        map会生成一个跟原来数据想对应的新队列
        filter不一定，只要符合条件的才会进入新的数据集合
    - filter函数怎么写：
        利用给定函数进行判断
        返回值一定是个布尔值
        调用格式： filter(f, data), f是过滤函数， data是数据
'''

# filter案例
'''
# 对于一个列表，对其进行过滤，偶数组成一个新列表
# 需要定义过滤函数
# 过滤函数要求有输入，返回布尔值
'''
def isFilt(a):
    return a % 2 == 0
l5 = [34,222,4455,3286,3,86,2000,1002442,57,235,57]
rst1 = filter(isFilt,l5)
# 返回结果是可迭代的列表
print(rst1)
# 需要用列表生成式打印出来列表的具体的元素
print ([f for f in rst1])

    # 系统高阶函数---sorted 排序
'''
把一个序列按照给定算法进行排序
key: 在排序前对每一个元素进行key函数运算，可以理解成按照key函数定义的逻辑进行排序
python2 和 python3 相差巨大
语法：sorted(列表, key=None, reverse=False（默认为升序排序）)
'''
help(sorted)
# 排序案例1、
l6 = [12,9,2353,345,111,35678,46]
l7 = sorted(l6)
# 默认reverse = False ，升序排列，可为空
print (l7)
# reverse=True ,降序排列
l8 = sorted(l6,reverse = True)
print(l8)

# 排序案例2、
l9 = [-43,-540,-3,4,13,220,9990]
# key=bas，按照绝对值排序，同时reverse=Trus降序排列
l10 = sorted(l9,key=abs, reverse=True)
print(l10)

# 排序案例3
l11 =['danne','Ndie','liwupu','guomi','BENDBE','Ndie11']
# reverse=False 默认字母升序排列，先大写，再小写字母
l12 = sorted(l11)
print(l12)
# key=str.lower 默认字母升序排列，先小写，再大写字母
l13 = sorted(l11,key=str.lower)
print(l13)