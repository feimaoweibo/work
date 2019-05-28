'''
- 系列化（持久化、落地）：把程序运行中的信息保存在磁盘上
- 反序列化：序列化的逆过程
- pickle：Python提供的序列化模块
-pickle.dump ：序列化
-pickle.load ：反序列化
'''
# 序列化案例1、
import pickle
age = 19
with open(r'test05.txt', 'wb') as f: # 'wb'表示以二进制格式写入
    pickle.dump(age, f)

# 反序列化案例2、
with open(r'test05.txt', 'rb') as f:
    age = pickle.load(f)
    print(age)

# 序列化案例3、
a = [19, 'liuang', 'i love goal', [123,34]]
with open(r'test05.txt', 'wb') as f:
    pickle.dump(a, f)

# 反序列化案例4、
with open(r'test05.txt', 'rb') as f:
    a = pickle.load(f)
    print(a)