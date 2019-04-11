# 数字开头模块
'''
- 包含一个学生类
- 一个sayhello函数
- 一个打印语句
'''
class Student():
    def __init__(self,name='noname',age=18):
        self.name = name
        self.age = age
    def say(self):
        print('My name is {0}'.format(self.name))
def sayHello():
    print('Hi,欢迎学习Python')

print('我是数字开头888模块')