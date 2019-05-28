'''
- 持久化工具：shelve模块
- 类似字典，用K-V 键值对 格式保存数据，存取方式跟字典也类似
- open():打开文件
- close():关闭文件
- r: 表示后面字符串内容不需要转义（必须）
- 格式： name = shelve.open(r'file.txt')
'''
import shelve

# 打开文件案例，同时发现shelve自动创建的不仅仅一个shv.db文件，还包括其他格式的文件
shv = shelve.open(r'shv.db')
shv['one'] = 1
shv['two'] = 2
shv['three'] = 3
shv.close()

# 读取文件案例
shv = shelve.open(r'shv.db')
try:
    print(shv['one'])
    print(shv['threeee'])
except Exception as e:
    print('查询的键，输入错误')
finally:
    shv.close()
print('-------1'*8)

# 二、shelve特性
'''
- 不支持多个应用并行写入
    - 为了解决这个问题，open的时候可以使用flag=r
- 写回问题
    - shelve情况下不会等待持久化对象进行任何修改
    - 解决方法： 强制写回：writeback = True
'''
    # shelve：案例之只读打开
shv = shelve.open(r'shv.db', flag='r')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()
print('-------2.1---------')
shv = shelve.open(r'shv.db')
try:
    shv['one'] = {'eine':1, 'zwei':2, 'drei':3}
    print(shv['one'])
finally:
    shv.close()
shv = shelve.open(r'shv.db')
try:
    one2 = shv['one']
    print(one2)
finally:
    shv.close()
print('--------2.2---------')

    # shelve:案例之强制写回
# shelve 忘记写回案例，数据任然未发生变化，需要使用强制写回
shv = shelve.open(r'shv.db')
try:
    k2 = shv['one']
    print(k2)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k2['eins'] = 100
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    k2 = shv['one']
    print(k2)
finally:
    shv.close()
print('---------2.3-----------')

# shelve 忘记写回，使用强制写回案例
shv = shelve.open(r'shv.db', writeback=True)
try:
    k3 = shv['one']
    k31 = shv['three']
    print(k3)
    print(k31)
    k3['eine'] = 100
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    #k3 = shv['one']
    print(k3)
finally:
    shv.close()
print('------------2.4-----------')
# shelve 使用with管理上下文环境
with shelve.open(r'shv.db', writeback=True) as shv:
    k4 = shv['one']
    k5 = shv['two']
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    print(k4)
    print(k5)
    k4['eine'] = 1000
with shelve.open(r'shv.db') as shv:
    print(shv['one'])