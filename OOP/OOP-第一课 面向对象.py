# OOP-Python面向对象
'''
- 面向对象编程
    -基础
    -共有私有
    -继承
    -组合、Mixin
- 魔法函数
    -魔法函数概述
    -构造类魔法函数
    -运算类魔法函数
'''
# 1.面向对象概述（ObjectOriented）
'''
- OOP思想
    -接触到任意一个任务，首先想到的是任务这个世界的构成，是由模型构成的
- 几个名词
    -OO: 面向对象
    -OOA: 面向对象的分析
    -OOD: 面向对象的设计
    -OOI: XXX的实现
    -OOP: XXX的编程
    -OOA->OOD->OOI:面向对象的实现过程
- 类和对象的概念
    - 类：抽象名词，代表一个集合，共性的事务
    -对象：具象的食物，单个个体
    - 类与对象的关系
        - 一个具体，代表一类事务的某一个个体
        - 一个是抽象，代表的是一大类事物
- 类中的内容，应该具有2个内容
    - 表面事物的特征，叫做属性（变量）
    - 表面事物功能或者动作，称为成员方法（函数）
'''
# 2. 类的基本实现
'''
- 类的命名
    - 遵守变量命名的规范
    - 大驼峰（由一个或者多个单词构成，每个单词首字母大写，单词与单词直接相连）
    - 尽量避开系统命名相似的命名
- 如何声明一个类
    -必须用class关键字
    -类由属性和方法构成，其他不允许出现
    -成员属性定义可以直接使用变量赋值，如果没有，允许使用None
    -函数末尾推荐使用return语句
    
'''
# 例子
class Student():
    #一个空类，pass代表直接跳过
    #pass必须由
    pass
#实例化一个对象
mingyue = Student()

class PythonStuent():
    name = None
    age =18
    course ="Python"
    def DoHomework(self):
        print("I 在做作业")
        #推荐在函数末尾使用return语句
        return None
'''
 -实例化一个对象
 -与类齐平
 -变量 = 类名（） 
 -访问对象成员
    -obj.成员属性名称
    -obj.成员方法
 -可以通过默认内置变量检查类和对象的所有成员
    -对象所有成员检查
        # dict 前后各有2个下划线
        obj.__dict__
    -类所有的成员
        # dict 前后各有2个下划线
        obj.__dict__
'''
yueyue = PythonStuent()
print(yueyue.age)
print(yueyue.name)
yueyue.DoHomework()
PythonStuent.__dict__