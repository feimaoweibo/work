    # 一、zip函数 把两个可迭代的内容生成一个可迭代的tuple（元组）元素类型组成的内容
# 案例1、
l1 = [1,2,3,4,5]
l2 = [11,22,33,44,55]
z = zip(l1,l2)
print(type(z))
print(z)
# 用for循环遍历出可迭代的元组列表
for i  in  z:
    print(i)

# 案例2、
l3 = ['wangxiaojing','panxueying','leilei']
l4 = [89,23,43]
z1 = zip(l3,l4)
# 方案一用for循环遍历出可迭代的元组列表
'''
for i in z1:
    print(i)
'''
# 方案二用列表生成式打印元组列表
l5 = [i for i in z1]
print(l5) # 打印结果为 空[]
print('-----zip函数'*5)

    # 二、enumerate 函数
'''
- 跟zip功能比较像
- 对可迭代对象里的每一元素，配上一个索引，然后索引和内容构成tuple类型
'''
# 例子1、默认索引值从0开始
l6 = [11,33,55,77,99]
em = enumerate(l6)
print(em)
# 方案一 使用for循环遍历出可迭代的元组列表
'''
for e in em:
    print(e)
'''
# 方案二 使用列表生成式打印元组列表
l7 = [e for e in em]
print(l7)

#例子2、可以指定索引值的开始值 enumerate([列表]，start='开始值（int类型）')
em2 = enumerate(l6,start=100)
l8 = [e2 for e2 in em2]
print(l8)
print('-----enumerate函数'*5)

    # 三、collections模块
'''
- namedtuple
    - tuple 类型
    - 是一个可命名的tuple
- deque
    - 解决频繁删除插入带来的效率问题
- defaultdict
    - 当直接读取dict不存在的属性时，直接返回默认值
- counter
    - 统计字符串个数
'''
import collections
#例子1、collections.namedtuple() 给元组元素赋值
point = collections.namedtuple('point',['x','y'])
# 给元组的元素赋值
p = point(11,22)
print(p)
print(p.x)
print(p.y)
print(p[0])
print(p[1])
# 例子2、
point1 = collections.namedtuple('point1',['a','b','c'])
p1 = point1(100,150,50)
print(p1)

#例子2、deque 解决增删改带来的效率问题
from collections import deque
q = deque(['a','b','c'])
print(q)
# 元组列表添加新元素
q.append('d')
print(q)
# 元组列表前面添加新元素
q.appendleft('x')
print(q)

#例子3、 defaultdict ,解决字典读取时没有对应键时，避免报错，默认返回自定义的默认值
from collections import defaultdict
d1 = {'one':1 ,'two':2, 'three':3}
print(d1['one'])
# print(d1['four']) 此时d1(['four']) 系统会报错
# 解决方案：使用 defaultdict(参数)来默认查找键时不存在的结果值
func = lambda: "创建查询时不存在的键时，返回的默认值"
d1 = defaultdict(func)
print(d1['four'])
print('-----collections模块'*5)

#例子4、Counter 模块 统计字符串个数
from collections import Counter
c = Counter("abmdingixinailsingerinsialinlrg")
print(c)
