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
s = Student("周周", 22, (89,76,97.5))
print(s.get_name())
print(s.get_age())
print(s.get_sourse())

print("----1----    "*5)
# 2、定义一个字典类：DictClass，完成如下操作：
'''
1、删除某个key: del_dict
2、判断某个键是否在字典里，如果在返回键对应的值，不在则返回“not found”:get_dict
3、返回键组成的列表，返回类型：list get_key
4、合并字典，并且返回合并字典的values组成的列表，返回类型：list updeta_dict

'''
class DictClass():
    def __init__(self,dict):
        self.dict = dict
    def del_dict(self,key):
        if key not in self.dict.keys():
            return "key 不在列表里"
        else:
            self.dict.pop(key)
            return "删除成功"
    def get_dict(self,key):
        if key not in self.dict.keys():
            return  "nof found"
        else:
            return self.dict[key]
    def get_key(self):
        return self.dict.keys()
    def update_dict(self,dict2):
        self.dict = dict(self.dict, **dict2)
        return self.dict.values()

d = DictClass({"a":1,"b":2})
print(d.del_dict("e"))
print(d.get_dict("a"))
print(d.get_key())
print(d.update_dict({"c": 3}))

print("----2----    "*5)

# 3、定义一个列表的操作类 Listinfo
'''
- 列表元素添加：add_key()
- 列表元素取值：get_key()
- 列表合并：update_list(list)
- 删除并且返回最后一个元素:del_key()
'''
class Listinfo():
    def __init__(self, list_val):
        self.list = list_val
    def add_key(self, key_name):
        self.list.append(key_name)
        print(self.list)
        return  "OK"
    def get_key(self, index):
        # index 索引列表里的值，顺序从0开始
        if index >= 0 and index < len(self.list):
            return self.list[index]
        else:
            print("你输入的数字带多了")

    def update_list(self, new_list):
        self.list = self.list + new_list
        return self.list
    def del_key(self,key):
        if len(self.list) >= 0:
            # .pop()删除列表里最后一个值
            return self.list.pop(-1)
        else:
            print("列表是空的")

l = Listinfo([1,2,3,4,5])
print(l.add_key(6))
print(l.get_key(3))
print(l.update_list([8,9,10]))
print(l.del_key(-2))
print("----3----    "*5)

# 4、定义一个集合的操作
'''
- 集合元素的添加：add_settinfo()
- 集合的交集：get_intersettinfo()
- 集合的并集：get_union()
- 集合的差集：get_difference()
'''
class SettInfo():
    def __init__(self,my_sett):
        self.sett = my_sett
    def add_settinfo(self,mysett):
        # 集合添加元素 add()
        self.sett.add(mysett)
        return self.sett
    def get_intersettinfo(self,jiaoji):
        # 集合交集 & 符号取值
        return self.sett & jiaoji
    def get_union(self,jiaoji):
        # 集合并集 | 符号取值
        return self.sett | jiaoji
    def get_difference(self,jiaoji):
        # 集合差集 - 符号取值
        return self.sett - jiaoji
na_set = {1,2,3,4,5}
jiao_set = {5,3,7,9}
mysett = SettInfo(na_set)
# 集合元素添加
print(mysett.add_settinfo(6))
# 取集合交集
print(mysett.get_intersettinfo(jiao_set))
# 取集合并集
print(mysett.get_union(jiao_set))
# 取集合的差集
print(mysett.get_difference(jiao_set))

print("-----4-----     "*5)

# 5、练习题- 创建北京和成都两个校区
'''
创建Linux\Python两个课程
创建北京校区的Python 3期课程和成都校区的Linux 1期课程
管理员创建了北京校区的学员小张，并将其分配在了Python 3期
管理员创建了讲师小周，并将其分配给了Python 3期
讲师小周创建了一条 Python 3期的上课记录 Day02
讲师小周为Day02 这节课所有的学员批改了作业， 小张得了A，小王得了B
学员小张查看了自己所报的课程
学员小张在 查看了 自己在Python 3 的成绩列表然后退出了
学员小张给了讲师小周好评
'''
class School():
    def __init__(self, school_xiaoqu, school_text, school_stu, school_teach):
        self.school_xiaoqu = school_xiaoqu
        self.school_text = school_text
        self.school_teach = school_teach
        self.school_stu = school_stu

    def creatzone(self,shcool_xiaoqu):
        self.school_xiaoqu.append(xiaoqu.name)
        print("我们开设有北京校区")
