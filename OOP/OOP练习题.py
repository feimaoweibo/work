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
# 定义一个课程列表
Course_list = []
# 创建一个学校类
class School():
    def __init__(self, school_xiaoqu,):
        # 构造函数，包含学校，教师，学生
        self.school_xiaoqu = school_xiaoqu
        self.school_teach = []
        self.school_stu = []
    # 声明课程列表是全局变量
    global Course_list
    # 创建学校的教师
    def creatteach(self,obj):
        self.school_teach.append(obj.name)
        print("我们聘请了一个新老师{}".format(obj.name))
    # 创建学校的学生
    def creatstu(self, obj):
        self.school_stu.append(obj.name)
        print("我们新招了一个学员{}".format(obj.name))
# 定义学校校区的类
class SchoolWork(School):
    # 构造函数，包括校区、培训期数、培训课程
    def __init__(self, school_xiaoqu, peixun_date, peixun_kecheng):
        # super() 调用父类函数
        super(SchoolWork,self).__init__(school_xiaoqu)
        self.kecheng = peixun_kecheng
        self.date =peixun_date
        self.menbers = []
        # 新增课程添加到课程列表里，使用.append() 函数
        Course_list.append(self.kecheng)
        print("我们现在{}校区开设了{}年级的{} 课程".format(self.school_xiaoqu,self.date,self.kecheng))

    def info_dagang(self):
        print("课程大纲{}day01, day02, day03".format(self.kecheng))
# 实例化一个培训课程，分别是Python、linux,以及分别所属校区、培训期数
Python = SchoolWork("北京", 3, 'Python')
Linux = SchoolWork("成都", 1, "Linux")
# 创建一个学校成员类
class SchoolMenber():
    # 构造函数，实例化成员包括姓名、年龄、性别、角色
    def __init__(self,name,age,sex,role):
        self.name = name
        self.age =age
        self.sex =sex
        self.role =role
        self.Course_list = []
        print("我叫{}，我是一个{}".format(self.name,self.role))
# 定义学生ID变量默认为0
stu_num_id = 00
# 创建学生类
class Students(SchoolMenber):
    # 构造函数，实例化学生的姓名、年龄、性别、角色、课程
    def __init__(self,name,age,sex,role,kecheng):
        # super() 调用父类函数
        super(Students, self).__init__(name,age,sex,role)
        # 声明学生ID为全局变量
        global stu_num_id
        stu_num_id +=1
        # ID的构成为校区课程+学生角色+培训期数+学生ID， zfill()函数 为填充函数，当只有一位数时前面填充0，只能用在str类型
        stu_id =kecheng.school_xiaoqu + "S" + str(kecheng.date) + str(stu_num_id).zfill(2)
        self.id =stu_id
        # 成绩列表
        self.mark_list = {}
    # 学习的课程已经学号
    def study(self, kecheng):
        print("我来这里学习{}课，我的学号是{}".format(kecheng.kecheng, self.id))
    # 报名课程的学费
    def pay(self, kecheng):
        print("我交了5800元的{}课学费".format(kecheng.kecheng))
        # 添加报名课程到课程列表
        self.Course_list.append(kecheng.kecheng)
    # 对所学课程老师的评价
    def praise(self, obj):
        print("{}觉得{}课很值得学习".format(self.name, obj.name))
    # 查看自己成绩
    def mark_check(self):
        for i in self.mark_list.items():
            print(i)

    def out(self):
        print("我离开了")
# 定义教师默认的ID
teach_num_id = 00
# 创建教师类
class Teachers(SchoolMenber):
    # 构造函数实例化教师，包括名字、年龄、性别、角色、教授课程
    def __init__(self,name,age,sex,role,kecheng):
        # super()调用父辈函数，包括姓名、年龄、性别、角色
        super(Teachers,self).__init__(name,age,sex,role)
        # 声明教师ID为全局变量
        global teach_num_id
        teach_num_id += 1
        # 同学生ID构成
        teach_num_id = kecheng.school_xiaoqu + "T" + str(kecheng.date) + str(teach_num_id).zfill(2)
        self.id = teach_num_id
    # 教授课程和教师ID
    def teach(self,kecheng):
        print("我来这里讲{}课程，我的ID是{}".format(kecheng.kecheng, self.id))
    # 给学员课程打分
    def record_mark(self,date,kecheng,obj,level):
        obj.mark_list["Day" + date] = level
print("****----****    "*4)
# 实例化学生，包括姓名、年龄、性别、角色、课程
a = Students("小张",18,"M",'student',Python)
# 注册学员小张
Python.creatstu(a)
# 小张学习的课程和他的学号
a.study(Python)
# 小张报名学费
a.pay(Python)
print("****----****    "*4)
b = Students("小王",22,"F","student",Python)
Python.creatstu(b)
b.study(Python)
b.pay(Python)
print("****----****    "*4)
# 实例化教师，包括姓名、年龄、性别、角色、教授课程
t = Teachers("小周",30,"M","teacher",Python)
# 注册教师小周
Python.creatteach(t)
# 教授课程和教师ID
t.teach(Python)
# 分别创建学员小王和小张的培训课程成绩
t.record_mark("1",Python,a,"A")
t.record_mark("1",Python,b,"A")
print("小王查看了自己的课程")
# 打印小王的课程
print(b.Course_list)
print("小王查看了自己的成绩")
# 打印小王的培训课程成绩
b.mark_check()
print("小王退出了")
# 打印小王推出培训
b.out()
print("给好评")
# 打印小王对教师小周的评价
b.praise(t)