import math
# print(100)
# ceil() 向上取整
'''
print(math.ceil(5.01))
print(math.ceil(5.9))

# floor() 向下取整
print(math.floor(5.01))
print(math.floor(5.9))
# 查看系统保留关键字，不可以用来当作变量的命名
import keyword
print(keyword.kwlist)

# round() 四舍五入
print(round(5.01))
print(round(5,5))
print(round(5.8))
# fsum() 对整个序列求和 ,返回值由本身类型而定
print(math.fsum([1,4,5,7]))

# sum() python内置求和  返回值由本身类型而定
print(sum([1,4,5,7]))

# math.modf() 将一个浮点数拆分为整数部分与小数部分组成 ,小数部分在前，整数部分在后
print(math.modf(4.5))
print(math.modf(0.3))
print(math.modf(3))
print(math.modf(9.3))
# copysign() 将第二个数的符号（正负号）传给第一个数
print(math.copysign(2,-3))
print(math.copysign(-2,-3))
print(math.copysign(-2,3))
print(math.copysign(2,3))
# sqrt() 开平方 ，返回浮点数
print(math.sqrt(9))
# pow( ) 与幂运算差不多，计算一个数的几次方，有2个参数，第一个是底数，第二个是指数
print(math.pow(4,3))

print(math.pow(3,3))

import random
# random() 获取0-1之间的随机小数，包含0不包含1
for i in range(1,10):
    print(random.random())
    print(random.randint(1,9))# 制定开始和结束的数字，随机取得整数数字

print("* "*20)
# random.randrange() 获取指定开始和结束之间的值，同时也可以制定间隔值
for i in range(10):
    print(random.randrange(1,9,3))

# choice() 随机获取列表中的值
print(random.choice([1,55,345,88888,0]))
# shuffle() 随机打乱序列 返回值是空
list1 =  [34,890,54,1,7777777]
print(list1)
random.shuffle(list1)
print(list1)
'''

#作业题
#输入三位数，并于系统给出随机数字比较大小，大于给出的随机数，打印今晚可以买彩票了，小于打印你猜错了。
import random
num = input("请输入三位数字")
for i in range(1,2):

    list1 = print(random.randrange(100,999))
int(i) = list1
if int(num) > int(i):
    print("今晚可以买彩票了")
else:
    print("你猜错了")

