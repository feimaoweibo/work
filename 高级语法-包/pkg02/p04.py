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
if __name__ == '__main__':
    print('我是第二个包里面的模块p04')