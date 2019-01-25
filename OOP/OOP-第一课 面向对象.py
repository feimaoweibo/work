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
    - 对象：具象的食物，单个个体
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
    - 必须用class关键字
    - 类由属性和方法构成，其他不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有，允许使用None
    - 函数末尾推荐使用return语句
    
'''
# 例子1
'''
定义一个学生类，用来形容学生
'''
class Student():
    #一个空类，pass代表直接跳过
    #pass必须有
    pass
#实例化一个对象
mingyue = Student()
# 定义一个类，用来描述听python的学生
# 注意缩进层级
# 系统默认一个self 参数
class PythonStuent():
    #None 给不确定的值赋值
    name = None
    age =18
    course ="Python"
    def DoHomework(self):
        print("I 正在看视频学习呢")
        #推荐在函数末尾使用return语句
        return None
# 实例化一个学生
yueyue = PythonStuent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传递参数
yueyue.DoHomework()
print("--------2.1---------"*3)
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
        class_name.__dict__
'''

# 4. 类和对象的成员分析
'''
- 类和对象都可以存储成员，成员可以归类所有，也可以归对象所有
- 类存储成员时使用的是与类关联的一个对象
- 独享存储成员时存储在当前对象中
- 对象访问一个成员时，如果对象中的没有该成员，尝试访问类中的同名成员
  如果对象中有此成员时，
- 创建对象的时候，类中的成员不会放入对象当中，而是得到一个空对象，没有成员
- 通过对象对类中的成员重新赋值或者通过对象添加成员时，对应成员会保存在对象中，而不会修改类成员

'''
# 例子2
class Student():
    name = "dana11"
    age = 181
print(Student.__dict__)
# 实例化
yueyue = Student()
print(yueyue.__dict__)
print(yueyue.name)


print("--------4.1---------"*3)
class Student():
    name = "danan"
    age = 18
Student.__dict__

# 实例化
yueyue = Student()
yueyue.__dict__
print(yueyue.name)
print("--------4.2---------"*3)

class A():
    name = "dana4.2"
    age =18
    # 注意say的写法，参数有一个self
    def say(self):
        self.name ="aaaa11"
        self.age =200
# 此案例说明
# 类实例的属性和其对象的实例的属性，在不同对象的实例属性赋值前提下，指向同一个变量
# 此时，A成为类实例
print(A.name)
print(A.age)

print("* "*5)
# id 可以鉴别
print(id(A.name))
print(id(A.age))
print("* "*10)

a = A()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print("*  "*15)
# 通过对象对类中的成员重新赋值或者通过对象添加成员时，对应成员会保存在对象中，而不会修改类成员
a = A()
a.name = "danna4.3333"
a.age = 133
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print("---------4.3---------"*3)


# 5. 关于self
'''
- self 在对象的方法中，表示当前对象本身,如果通过对象调用一个方法，
  那么该对象会自动传到当前方法的的第一个参数中
- self 不是关键字，只是用于接受对象的普通参数，理论上可以用任何普通变量代替
- 方法中self形参的方法成为非绑定类的方法，可以通过对象访问，没有self的是绑定类的方法，只能通过类访问
- 使用类访问绑定类的时，如果类方法中需要访问当前类的成员，可以通过__class__成员名来访问


'''
# 案例3-对1、2点说明
class Student():
    name = "dana2222"
    age =183

    # 注意say的写法，参数由一个self
    def say(self):
        self.name ="aaaa"
        self.age =200
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))

    def sayAgain(s):
        print("My name is {0}".format(s.name))
        print("My age is {0}".format(s.age))
yueyue = Student()
yueyue.say()
yueyue.sayAgain()
print("-----------5.1----------"*4)
# 案例4 -对3、4点说明
class Teacher():
    name = "dana111"
    age = 19

    def say(self):
        self.name ="yaona1111"
        self.age = 1711
        print("my name is {0}".format(self.name))
        # 调用类的成员变量需要用 __class__
        print("ma age is {0}".format(__class__.age))
    def sayAgain():
        # 调用类的成员变量需要用 __class__
        print(__class__.name)
        print(__class__.age)
        print("hello,nice to see you again")
t = Teacher()
t.say()
Teacher.sayAgain()

print("-----------5.2---------"*3)
# 案例3-self函数
class A():
    name = "liuying"
    age  = 18

    def __init__(self):
        self.name = "aaaa"
        self.age = 200
    def say(self):
        print(self.name)
        print(self.age)
class B():
    name = "bbbb"
    age = 90
a = A()
# 此时，系统会默认把a作为第一个参数传入函数
a.say()
# 此时，self被a替换
A.say(a)
# 同样可以把A作为参数传入
A.say(A)
# 此时，传入的是类实例B，因为B具有name和age属性，所以不会报错
A.say(B)
# 以上代码，利用了鸭子模型
print("----------5.3-------------"*3)



# 6. 面向对象的三大特性
'''
- 封装
- 继承
- 多态

'''
'''
# 6.1 封装
- 封装就是对对象的成员进行访问限制
- 封装的三个级别：
    - 公开 public
    - 受保护的 protected
    - 私有的 private
    -以上三个不是关键字
- 判别对象的位置
    - 对象内部
    - 对象外部
    - 子类中
- 私有 private
    - 私有成员时最高级别的封装，只能在当前类或对象中访问
    - 在成员前面添加两个下划线即可
        class Person():
            name = "liuying" #共有成员 
            #__age 就是私有成员
            __age = 18
    - Python 的私有不是真私有，是一种称为name mangling的改名策略
        可以使用对象._classname_attributename访问
- 受保护的 protected
    - 受保护的封装是蒋对象成员进行一定级别的封装，然后，在类中或者子类都可以进行访问，再是在外出都不可以
    - 封装方法：在成员名称添加一个下划线即可
- 公开的 public
    -公共的封装实际对成员没有任何操作，任何地方都可以访问
# 6.2 继承
- 继承就是一个类可以获得另外一个类中的成员属性或成员方法
- 作用：减少代码，增加代码的复用功能，同时可以设置类与类直接的关系
- 继承与被继承的概念
    - 被继承的类叫父类，也叫基类，也叫超类
    - 用于继承的类，交子类，也叫派生类
    - 继承与被继承的关系，is->A
- 继承的特征
    - 所有的类都继承自object类，即所有的类都是object类的子类
    - 子类一旦继承父类，则可以使用父类中除私有成员外的所有内容
    -子类继承父类后并没有将父类成员完全赋值到子类中，而是通过饮用关系访问调用
    - 子类中可以定义独有的成员属性
    - 子类中定义的成员和父类成员如果相同，则优先使用子类成员
    - 子类如果想扩充父类的方法，可以在定义新方法的同时访问父类成员来进行代码重用，
        可以使用 [父类名.父类]成员 的格式调用父类成员，也可使用super（）.父类成员的格式来调用
- 继承变量函数的查找顺序
    - 优先查找自己变量
    - 没有查找父类
    - 构造函数查找如果本类中没有定义，则自动查找调用父类构造函数
'''
# 6.1 公、私有案例说明
class PersonEnjoy():
    # 共有成员
    name = "liuying"
    # __age 就是私有成员
    __age = 18

t = PersonEnjoy()
print(t.name)
# __age 就是私有成员
# print(t.__age)
# 真要访问，使用_class类名形式来访问
t._PersonEnjoy__age = 190
print(t._PersonEnjoy__age)


print("----------6.1-------------"*3)

# 6.2 继承案例 1----子类一旦继承父类，则可以使用父类中除私有成员外的所有内容
class Person():
    name ="noname"
    age =0
    def sleep(self):
        print("sleeping")
# 父类写在括号里
class Teacher(Person):
    pass
t = Teacher()
print(t.name)
print(Teacher.name)
print("----------6.2-------------"*3)
# 继承案例 2----子类中可以定义独有的成员属性
class Person():
    name ="noName1111"
    age = 0
    # __socre 分数是私密，不能外部访问，只能自己知道
    __socre = 61
    # _petname 小名是受保护的，子类可以用，但不能公用
    _petname = "小名，受保护的，应该不能公用"
    def sleep(self):
        print("sleeping")
# 父类写在括号里
class Teacher(Person):
    # 子类中可以定义独有的成员属性
    teacherid = "003452"
    def work(self):
        print("我出试题考你们")
t = Teacher()
print(t.name)
# _petname 小名是受保护的，不能公用，！！！！
# print(t._petname)
t.sleep()
print(t.teacherid)
t.work()
print("---*****---6.2---****----" * 3)

# 继承案例 3---子类如果想扩充父类的方法，可以在定义新方法的同时访问父类成员来进行代码重用，-
class Person():
    name ="noName1111"
    age = 0

    def sleep(self):
        print("sleeping")
    def work(self):
        print("挣钱买东西吃撒")
    def work1(self):
        print("存钱取婆娘")
# 父类写在括号里
class Teacher(Person):
    # 子类中可以定义独有的成员属性
    teacherid = "003452"
    def work_mark(self):
        print("我出试题考你们")
    def work(self):
        # 扩充父类的功能可以使用【父类名.对应函数】格式或者使用 super().对应函数的方式
        Person.work(self)
        super().work1()
        self.work_mark()
t = Teacher()
t.work()
print("*****---6.2---****" * 3)


'''
- 6.2.2 构造函数
    - 是一类特殊的函数在类进行实例化之前进行调用
    - 如果定义构造函数，则实例化时使用构造函数，不查找父类构造函数
    -  如果没定义，则自动查找父类构造函数
    - 如果子类没定义，父类的构造函数带参数，则构造对象时的参数应该按父类参数构造
'''
# 构造函数例子
# 构造函数的调用顺序
# 如果子类没有写构造函数，则自动向上查找，直到找到位置

# 6.2.2 继承类中的构造函数例子 1、
class Dog():
    #__init__是构造函数
    # 每次实例化的时候，第一个被自动调用
    def __init__(self):
        print("i an init in dog")
kakkkk = Dog()
print("----6.2.2-----    "*5)

# 6.2.2 继承类中的构造函数例子 1-如果没定义，则自动查找父类构造函数
class Animel():
    def __init__(self):
        print("Animel")
class PaxingAni():
    def __init__(self):
        print("PaxingDongwu")
class DDog(PaxingAni):
    def __init__(self):
        print(" 我是狗类动物")
dog = DDog()
class Mat(PaxingAni):
    pass

cat = Mat()
print("----6.2.3-----    "*5)

'''
-6.3 super
    - super 不是关键字，而是一个类
    - super的作用是获取MRO列表中的第一个类
    - super与父类直接没有任何实质关系，但通过super 可以调用到父类
    - super使用两个方法,参见在构造函数中调用父类的构造函数
-6.4 单继承和多继承
    - 单继承：每个类只能继承一个类
    - 多继承：每个类允许继承多个类
    - 单继承与多继承的优缺点
        - 单继承：
            - 传承有序逻辑清晰语法简单隐患少
            - 功能不能无限扩展，只能在当前唯一的继承链中扩展
        - 多继承：
            - 优点：类的功能扩展方便
            - 缺点：继承关系混乱
'''
# 6.4 多继承例子
class Fish():
    def __init__(self,name):
        self.name = name
    def swin(self):
        print("i am swimming......")
class Brid():
    def __init__(self,name):
        self.name = name

    def fly(self):
        print("i am flyying.......")
class Person():
    def __init__(self,name):
        self.name = name

    def work(self):
        print("working......")
# 单继承例子
class Student(Person):
    def __init__(self,name):
        self.name = name

class SuperMan(Person,Brid,Fish):
    def __init__(self,name):
        self.name = name
class SwimMan(Person,Fish):
    def __init__(self,name):
        self.name = name
# 多继承例子
s = SuperMan("yueyue")
s.fly()
s.swin()
# 单继承例子
stu =Student("yueyue")
stu.work()
print("----------6.4-------------"*3)

'''
-6.5 菱形继承/砖石继承问题
    - 多个子类继承自同一个父类，这些子类由被同一个类继承，于是继承关系图形成一个菱形
    - MRO
    - 关于多继承的MRO
        - MRO就是多继承中，用于保存继承顺序的一个列表
        - python本身采用C3算法来承接多继承的菱形继承进行计算结果
        - MRO列表的计算原则
            - 子类永远在父类前面
            - 如果多个父类，则根据继承语法中括号内的书写顺序存放
            - 如果多个类继承了同一个父类，孙子类张只会选取继承语法括号中第一个父类的父类
-6.6 构造函数
    - 在对象进行实例化的时候，系统自动调用的一个函数叫构造函数，通常此函数用来对实例
        对象进行初始化，顾名。
    - 构造函数一定要有，如果没有，则自动向上查找，按照MRO顺序，直到找到为止
'''
# 6.6 构造函数例子
class Person():
    # 对 person类进行实例化的时候
    # 姓名要确定
    # 年龄得确定
    # 地址得肯定
    def __init__(self):
        self.name = "noname"
        self.age = 18
        self.address = "studenthouse"
        print("构造函数：初始化实例时第一个自动调用函数")
# 实例化一个人
p = Person()

# 1、面例子说明构造函数调用顺序
class A():
    def __init__(self):
        print("A")
class B():
    def __init__(self):
        print("B")
class C(B):
    pass
# 此时，首先查找C的构造函数
# 如果没有，则向上按照MRO顺序查找父类的构造函数，直到找到为止
c = C()

print("----6.6-----    "*5)

# 2、下面例子说明---注意调用父辈构造函数时，对应函数的参数数量
class A():
    def __init__(self):
        print("A")
class B(A):
    def __init__(self, name):
        print("B")
        print(name)
class C(B):
    pass
# 此时，首先查找C的构造函数
# 如果没有，则向上按照MRO顺序查找父类的构造函数，直到找到为止
c = C("注意调用父辈构造函数时，对应函数的参数数量")
print("-----6.6.1-----"*5)

# 3、在构造函数中调用父类构造函数来扩展自身函数功能，.可以用【类.函数名】和 super() 来实现
# 下例在C中调用B的函数后，添加一些自身函数功能
class A():
    pass
class B(A):
    def __init__(self,name):
        print("父类-B")
        print(name)

class C(B):
    def __init__(self,name):
        # 首选调用父类构造函数
        B.__init__(self, name)
        # 其次再增加自己的功能
        print("打印C中想实现扩展函数的功能---方法1【类名.函数名】形式"),

class D(B):
    def __init__(self,name):
        # 首选调用父类构造函数,注意传入参数的写法
        # 使用 super().__init__ 调用父类函数时，super()接受 新类+self 格式
        super(D,self).__init__(name)
        # 其次再增加自己的功能
        print("打印C中想实现扩展函数的功能---方法2【super()】"),
c = C("我是调用B中的")
print("-----方法分隔符--------")
d = D("我是调用B中的构造函数")
print("-----6.6.2----"*5)

'''    
# 6.7.多态
- 多态就是同一个对象在不同情况下有不同的状态出现
- 多态不是语法，是一种设计思想
- 多态性：一种调用方式，不同的执行效果
- 多态：同一事物的多种形态，如动物分为人类，狗类，猪类
- 多态与多态性：说明文档 https://www.cnblogs.com/luchuangao/p/6739557.html
- Mixin设计模式
    - 主要采用多继承方式对类的功能进行扩展
    - Mixin 概念 说明文档 https://www.zhihu.com/question/20778853
    - Mixin and Mro 说明文档  http://blog.csdn.net/robinjwong/article/details/48375833
    - Mixin 模式 说明文档 https://www.cnblogs.com/xybaby/p/6484262.html
    - Mixin Mro 说明文档 http://runforever.github.io/2014-07-19/2014-07-19-python-mixin%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/
    - MRO 说明文档 http://xiaocong.github.io/blog/2012/06/13/python-mixin-and-mro/
    - 我们使用多继承语法来实现Mixin
    - 使用Mixin实现多继承的时候非常小心
        - 首先他必须表示某一单一功能，而不是某个物品
        - 职责必须单一，如果有多个功能，则写多个Mixin
        - Mixin 不能依赖于子类的实现
        - 子类即使没有继承这个Mixin类，也能照样工作，只是缺少了某个功能
        

# 6.8 类相关函数
- issubclass:检测一个类是否是另一个类的子类
- isinstance:检测一个对象是否是一个类的实例
- hasattr:检测一个对象是否由成员xxx
- getattr: get attribute
- setattr: set attribute
- delattr: delete attribute
- dir: 获取对象的成员列表
'''

'''
-7. 类的成员描述符（属性）
    - 类的成员描述符是为了在类中对类的成员属性进行相关操作而创建的一种方式
        -get： 获取属性的操作
        - set：修改或者添加属性操作
        - delete： 删除属性的操作
    - 如果想使用类的成员描述符，大概有三种方法
        -使用类实现描述器
        -使用属性修饰符
        -使用property函数
            - property函数很简单
            - property(fget, fset, fdel, doc)
            -案例参看notebook
    - 无论哪种修饰符都是为了对成员属性进行相应的控制
        -类的方式： 适合多个类中的多个属性共用用一个描述符
        -property：使用当前类中使用，可以控制一个类中多个属性
        -属性修饰符： 使用于当前类中使用，控制一个类中的一个属性
- 8. 类的内置属性
    __dict__:以字典的方式显示类的成员组成
    __doc__: 获取类的文档信息
    __name__:获取类的名称，如果在模块中使用，获取模块的名称
    __bases__: 获取某个类的所有父类，以元组的方式显示
- 9. 类的常用魔术方法
    - 魔术方法就是不需要人为调用的方法，基本是在特定的时刻自动触发
    - 魔术方法的统一的特征，方法名被前后各两个下滑线包裹
    -操作类
        __init__: 构造函数
        __new__: 对象实例化方法，此函数较特殊，一般不需要使用
        __call__: 对象当函数使用的时候触发
        __str__: 当对象被当做字符串使用的时候调用
        __repr__: 返回字符串，跟__str__具体区别请百度
    -描述符相关
        __set__
        __get__
        __delete__
    - 属性操作相关
        __getattr__: 访问一个不存在的属性时触发
        __setattr__: 对成员属性进行设置的时候触发
            - 参数：
                - self用来获取当前对象
                - 被设置的属性名称，以字符串形式出现
                - 需要对属性名称设置的值
            - 作用：进行属性设置的时候进行验证或者修改
            - 注意： 在该方法中不能对属性直接进行赋值操作，否则死循环
            - 参看案例
    - 运算分类相关魔术方法
        __gt__: 进行大于判断的时候触发的函数
        - 参数：
            - self
            - 第二个参数是第二个对象
            - 返回值可以是任意值，推荐返回布尔值
        案例
- 10. 类和对象的三种方法
    - 实例方法
        - 需要实例化对象才能使用的方法，使用过程中可能需要截止对象的其他对象的方法完成
    - 静态方法
        -不需要实例化，通过类直接访问
    - 类方法
        - 不需要实例化
    - 参看案例
        - 三个方法具体区别自行百度
- 11. 所用软件
    -画图软件是Faststone capture
    -有问题加群 158184562
    -官网地址 www.tulingxueyuan.com
- 12.. 抽象类
    - 抽象方法： 没有具体实现内容的方法成为抽象方法

    - 抽象方法的主要意义是规范了子类的行为和接口

    - 抽象类的使用需要借助abc模块

        -import abc
    - 抽象类：包含抽象方法的类叫抽象类，通常成为ABC类

        - 抽象类的使用
            - 抽象类可以包含抽象方法，也可以包含具体方法
            - 抽象类中可以有方法也可以有属性
            - 抽象类不允许直接实例化
            - 必须继承才可以使用，且继承的子类必须实现所有继承来的抽象方法
            - 假定子类没有是现实所有继承的抽象方法，则子类也不能实例化
            - 抽象类的主要作用是设定类的标准，以便于开发的时候具有统一的规范
-13. 自定义类
    - 类其实是一个类定义和各种方法的自由组合
    - 可以定义类和函数，然后自己通过类直接赋值
    - 可以借助于MethodType实现
    - 借助于type实现
    - 利用元类实现- MetaClass
        - 元类是类
        - 被用来创造别的类
'''
