# 1、定义一个学生类，有下面的类属性
'''
- 姓名
- 年龄
- 成绩（语文、数学、英语）每科成绩类型为整数类方法
- 获取学生的姓名：get_name() 返回类型：str
- 获取学生的年纪：get_age() 返回类型：int
- 返回三门科目中最高的分数：get_sourse 返回类型：int
'''
class Student():
    def __init__(self,name,age,sourse):
        self.name = name
        self.age = age
        self.sourse = sourse
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_sourse(self):
        return max(self.sourse)
s = Student("周周", 22, (89,76,97))
print(s.get_name())
print(s.get_age())
print(s.get_sourse())
print("----1----    "*5)
