import math
# print(100)
# ceil() 向上取整
'''
print(math.ceil(5.01))
print(math.ceil(5.9))

# floor() 向下取整
print(math.floor(5.01))
print(math.floor(5.9))
# 查看系统保留关键字，不可以用来当作变量的命名
import keyword
print(keyword.kwlist)

# round() 四舍五入
print(round(5.01))
print(round(5,5))
print(round(5.8))
# fsum() 对整个序列求和 ,返回值由本身类型而定
print(math.fsum([1,4,5,7]))

# sum() python内置求和  返回值由本身类型而定
print(sum([1,4,5,7]))

# math.modf() 将一个浮点数拆分为整数部分与小数部分组成 ,小数部分在前，整数部分在后
print(math.modf(4.5))
print(math.modf(0.3))
print(math.modf(3))
print(math.modf(9.3))
# copysign() 将第二个数的符号（正负号）传给第一个数
print(math.copysign(2,-3))
print(math.copysign(-2,-3))
print(math.copysign(-2,3))
print(math.copysign(2,3))
# sqrt() 开平方 ，返回浮点数
print(math.sqrt(9))
# pow( ) 与幂运算差不多，计算一个数的几次方，有2个参数，第一个是底数，第二个是指数
print(math.pow(4,3))

print(math.pow(3,3))

import random
# random() 获取0-1之间的随机小数，包含0不包含1
for i in range(1,10):
    print(random.random())
    print(random.randint(1,9))# 制定开始和结束的数字，随机取得整数数字

print("* "*20)
# random.randrange() 获取指定开始和结束之间的值，同时也可以制定间隔值
for i in range(10):
    print(random.randrange(1,9,3))

# choice() 随机获取列表中的值
print(random.choice([1,55,345,88888,0]))
# shuffle() 随机打乱序列 返回值是空
list1 =  [34,890,54,1,7777777]
print(list1)
random.shuffle(list1)
print(list1)


#作业题
#输入三位数，并于系统给出随机数字比较大小，大于给出的随机数，打印今晚可以买彩票了，小于打印你猜错了。
import random
import math
num = input("请输入三位数字")
random_sjs = random.randrange(100,1000)
# print(random_sjs)
# print(type(random_sjs))
if num.isdigit() and 100 <= int(num) <= 999:
    if int(num) > random_sjs :
        print("比随机数大了")
    if int(num) == random_sjs:
        print("恭喜你猜中了")
    if int(num) < random_sjs :
        print("比随机数小了")
'''

'''
输入一个三位数与程序随机数比较大小
1、如果大于程序随机数，则分别输出这个三位数的个、十、百的数字；
2、如果等于程序随机数，则提示恭喜中奖了；
3、如果小于程序随机数，则打印120个字符，规则如下：
    a、每行字符串长度为12；
    b、前四个字符为字母；
    c、后八个字符为数字
'''
import random
import math

num = input("请输入一个三位数： ")
# 定义一个变量，把随机数赋值给它，作为程序随机数
random_sjs = random.randrange(100,1000)
if num.isdigit() and 100 <= int(num) <= 999: # .insdigit()函数用来判断输入内容是否是数字的先决条件
    if int(num) == random_sjs: # int()函数把输入数字用作为数字类型
        print("恭喜你，千分之一的中奖概率都给你碰上了")
    if int(num) > random_sjs:
        bai = int(num)//100    # “//”符号，表示整除，返回商的整数部分，即得到百位数上的数字
        shi = int(num)%100//10 # “%”符号，表示取模，返回除法的余数；比如num=333,num%100 ==33,表示先把333先除100得到余数33 ->再把33//10 ==3,表示把33整除10得到3为返回商的整数，即得到十位数上的数字
        ge  = int(num)%100%10  #  比如数字987,解析步骤：987%100==87，余数为87  -> 87%10==7,表示余数为7，即得到个位上的数字
        print("个位数是：{0}, 十位数是：{1},百位数是：{2}".format(ge,shi,bai))
    if int(num) < random_sjs:
        for l in range(11): # 根据要求打印120个字符，每行12个字符，需要打印10行
            str_t1 = '' # 定义一个变量，进行4次拼接动作存放字母字符，
            for i in range(4):
                str_name = random.randrange(65,123) # 定义变量用来存放65到122之间其中的一个数字
                str_ascii = chr(str_name) # 用chr()函数把acsii编码在65与122之间的数字，转换成52字母，包含大小写字母
                str_t1 =str_t1 + str_ascii # 拼接4次循环产生的字母
                # print(str_t1) 打印出每次转换后的字母
            # print(str_t1) 外层打印最后拼接4的字母
            str_t2 = ''
            for j in range(9):
                str_num = random.randrange(1,10)
                str_strnum = str(str_num)
                str_t2 =str_t2 + str_strnum
                # print(str_t2) 打印出每次循环随机生成的数字
            # print(str_t1) 外层打印最后一次循环生成的数字

            str_row = str_t1 + str_t2 # 拼接字母与数字

            print(str_row) # 打印10次生成的字母与数字组成的字符串



else:
    print('请重新输入一个三位数')