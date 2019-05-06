# 常用模块
'''
    # calendar
    # time
    # datetime
    # timeit
    # os
    # shutil
    # zip
    # math
    # string
    上述所有模块使用理论上都应该先导入，string是特例
    calendar，time，datetime的区别参考中文意思
'''
    # 1、calendar  跟日历相关的模块
import calendar
'''
    # calendar:获取一年的日历字符串
    # 参数
    # w = 每个日期之间的间隔字符数
    # l = 每周所占用的行数
    # c = 每个月之间的间隔字符数
'''
cal = calendar.calendar(2018)
print(cal)
cal1 = calendar.calendar(2018, w=5,l=1,c=10)
print(cal1)
    # isleap: 判断某一年是否是闰年
print(calendar.isleap(2018))
    # leapdays: 获取指定年份之间的闰年个数
print(calendar.leapdays(1998,2001))
    # month() 获取某个月的日历字符串
'''
格式： calendar.month(年，月)
回值：月 日历的字符串
'''
m1= calendar.month(2019,5)
print(m1)
    # monthrange() 获取一个月从周几开始及天数
'''
格式：calendar.monthrange(年，月)
回值：元组（周几开始，天数）
注意：周默认从0开始表示周一，6结束表示周天
'''
w,d = calendar.monthrange(2019,5)
print(w)
print(d)
    # monthcalendar() 返回一个月每天的矩阵列表
'''
格式：calendar.monthcalendar(年，月)
回值：二级列表
注意：矩阵中没有的天数，用0表示
'''
m = calendar.monthcalendar(2019,5)
print(m)
    # calendar.prcal(年) 直接打印日历
print(calendar.prcal(2019))
    # calendar.prmonth(年，月) 直接打印整个月的日历
print(calendar.prmonth(2019,4))
    # calendar.weekday(年，月，日) 直接打印具体日期是周几
print(calendar.weekday(2019,4,16))
print('---1---calendar模块结束---1---'*5)

    #2、 time 模块介绍
'''
时间戳
    - 一个时间表示，根据不同语言，可以是整数或者浮点数
    - 是从1970年1月1日0时0分0秒到现在经历的秒数
    - 如果表示的时间是1970年以前或者太遥远的未来，可能出现异常
    - 32位操作系统能够支持到2038年

UTC时间
    - UTC又称为世界协调时间，以英国的格林尼治天文所在地区的时间作为参考的时间，也叫做世界标准时间。
    - 中国时间是 UTC+8 东八区

夏令时
    - 夏令时就是在夏天的时候将时间调快一小时，本意是督促大家早睡早起节省蜡烛！ 每天变成25个小时，本质没变还是24小时

时间元组
    - 一个包含时间内容的普通元组
    索引    内容    属性         值
    0       年       tm_year     2015
    1       月       tm_mon      1～12
    2       日       tm_mday     1～31
    3       时       tm_hour     0～23
    4       分       tm_min      0～59
    5       秒       tm_sec      0～61  60表示闰秒  61保留值
    6       周几     tm_wday     0～6
    7       第几天   tm_yday     1～366
    8       夏令时   tm_isdst    0，1，-1（表示夏令时）
'''
import time
'''
    timezone:当前时区和UTC时间相差的秒数，在没有夏令时的情况下的间隔，东八区的是 -28800
    altzone : 获取当前时区与UTC时间相差的秒数，在有夏令时的情况下，
    daylight:测当前是否是夏令时时间状态, 0 表示是
'''
print(time.timezone)
print(time.altzone)
print(time.daylight)

    # 得到时间戳
print(time.time())
    # localtime 得到当前时间的时间结构，可以通过点号操作符得到相应的属性元素的内容
print(time.localtime())
t = time.localtime()
print(t.tm_hour)
    # asctime() 返回元组的正常的字符串化之后的时间格式
'''
格式：time.asctime(时间元组)
返回值：字符串 Sun Apr 28 16:10；17 2019
'''
tt = time.asctime(t)
print(type(tt))
print(tt)
    # ctime(): 获取字符串化的当前时间
t1 = time.ctime()
print(type(t1))
print(t1)
    # mktime() 使用时间元组获取对应的时间戳
'''
格式：time.mktime(时间元组)
返回值：浮点数时间戳
'''
ts = time.mktime(t)
print(type(ts))
print(ts)
    # clock: 获取CPU时间，3.0-3.3版本可直接使用，3.6调用有问题,使用process_time代替
print(time.process_time())
    # sleep: 是程序进入睡眠，n秒后继续
'''
-例子1
for i in range(10):
    print(i)
    time.sleep(2)

-例子2
def p():
    time.sleep(2.5)
t2 = time.process_time()
time.sleep(3)
t3 = time.process_time()
t4 = t3-t2
print(type(t4))
print(t4)
'''
    # strfime:将时间元组转化为自定义的字符串格式
'''
格式  含义  备注
%a  本地（locale）简化星期名称    
%A  本地完整星期名称    
%b  本地简化月份名称    
%B  本地完整月份名称    
%c  本地相应的日期和时间表示    
%d  一个月中的第几天（01 - 31）   
%H  一天中的第几个小时（24 小时制，00 - 23）   
%I  一天中的第几个小时（12 小时制，01 - 12）   
%j  一年中的第几天（001 - 366）  
%m  月份（01 - 12） 
%M  分钟数（00 - 59）    
%p  本地 am 或者 pm 的相应符    注1
%S  秒（01 - 61）  注2
%U  一年中的星期数（00 - 53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第 0 周   注3
%w  一个星期中的第几天（0 - 6，0 是星期天） 注3
%W  和 %U 基本相同，不同的是 %W 以星期一为一个星期的开始  
%x  本地相应日期  
%X  本地相应时间  
%y  去掉世纪的年份（00 - 99）    
%Y  完整的年份   
%z  用 +HHMM 或 -HHMM 表示距离格林威治的时区偏移（H 代表十进制的小时数，M 代表十进制的分钟数）      
%%  %号本身
'''
dayT = time.strftime('%Y.%m.%d %H:%M',t)
dayT1 = time.strftime("%Y{y}%m{m}%d{d} %H:%M").format(y='年',m='月',d='日') #涉及到使用中文字符的解析，用 .format()格式，不需要使用 时间结构t字符
dayT2 = time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')
print(dayT)
print(dayT1)
print(dayT2)
print('-----2----time模块'*5)

    # 3、datetime模块 提供日期和时间的运算和表示
import datetime
'''
- datetime 常见属性
    datetime.date: 一个理想和的日期，提供year，month，day 属性
'''
dt = datetime.date(2019,4,29)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)

'''
- datetime.datetime:提供日期跟时间的组合
    常用类方法：
        - today
        - now
        - utcnow
        - fromtimestamp:从时间戳中返回本地时间
'''
from datetime import datetime
dt1 = datetime(2019,4,28)
print(dt1.today)
print(dt1.now())
print(dt1.fromtimestamp(time.time()))

'''
- datetime.timedelta: 提供一个时间差，时间长度
'''
from datetime import datetime,timedelta
dt2 = datetime.now()
print(dt2.strftime('%Y-%m-%d %H:%M:%S'))
tl = timedelta(hours=1) # tl 表示以小时的时间长度
print((dt2+tl).strftime('%Y-%m-%d %H:%M:%S')) #当前时间加上时间间隔，把得到的一个小时后的时间格式化输出

print('-----4-----datetime'*5)

    # 4、timeit模块 时间测量工具

def p():
    time.sleep(3.6)
dt3 = time.time()
p()
print(dt3)
print(time.time() - dt3)

import timeit
    # 生成2个列表方法用时的比较，单纯比较生成列表的时间，可能很难实现
c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''
# 利用timeit调用代码，执行100000次，查看运行时间
dt4 = timeit.timeit(stmt='[i for i in range(1000)]',number = 100000)
# 测量代码C执行100000次运行所需时间
dt5 = timeit.timeit(stmt=c,number=100000)
print(dt4)
print(dt5)

    # timeit 可以执行一个函数，来测量一个函数的执行时间
'''
    例子1
def doIt():
    num = 3
    for i in range(num):
        print('Repeat for {0}'.format(i))
# 执行函数，重复10次
dt6 = timeit.timeit(stmt=doIt,number=10)
print(dt6)
'''
# 例子2
s ='''
def doIt1(num):
    for i in range(num):
        print('Repeat for {0}'.format(i))
'''
# 执行doIt1(num)
# setup负责把环境变量准备好
# 实际相当于给timeit创造了一个环境，在该环境中代码执行的顺序大概是，如下：
'''
def doIt1(num)
    ....
num =3 
doIt1(num)
'''
dt7 = timeit.timeit('doIt1(num)',setup=s + 'num=3',number=10)
print(dt7)

print('-----5-----timeit模块'*5)

    # 6、datetime.datetime 模块
'''
    - 提供比较好用的时间而已
    - 类定义
         class datetime.datetime(year, month, day[, hour
                  [, minute
                  [, second
                  [, microsecond
                  [, tzinfo]]]]])
        # The year, month and day arguments are required.
            MINYEAR <= year <= MAXYEAR
            1 <= month <= 12
            1 <= day <= n
            0 <= hour < 24
            0 <= minute < 60
            0 <= second < 60
            0 <= microsecond < 10**
    - 类方法
        datetime.today(): 返回当前本地datetime.
        随着 tzinfo None. datetime.fromtimestamp(time.time()). datetime.now([tz]): 返回当前本地日期和时间, 
        如果可选参数tz为None或没有详细说明,这个方法会像today(). datetime.utcnow(): 返回当前的UTC日期和时间, 
        如果tzinfo None ,那么与now()类似. datetime.fromtimestamp(timestamp[, tz]): 根据时间戳返回本地的日期和时间.tz指定时区. 
        datetime.utcfromtimestamp(timestamp): 根据时间戳返回 UTC datetime. 
        datetime.fromordinal(ordinal): 根据Gregorian ordinal 返回datetime. 
        datetime.combine(date, time): 根据date和time返回一个新的datetime. 
        datetime.strptime(date_string, format): 根据date_string和format返回一个datetime.
    - 实例方法
        datetime.date(): 返回相同年月日的date对象. 
        datetime.time(): 返回相同时分秒微秒的time对象. 
        datetime.replace(kw): kw in [year, month, day, hour, minute, second, microsecond, tzinfo], 与date类似. 
    
    - 类属性
        datetime.min: datetime(MINYEAR, 1, 1). 
        datetime.max: datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999).
    - 实例属性(read-only)
        datetime.year: 1 至 9999 
        datetime.month: 1 至 12 
        datetime.day: 1 至 n 
        datetime.hour: In range(24). 0 至 23 
        datetime.minute: In range(60). 
        datetime.second: In range(60). 
        datetime.microsecond: In range(1000000). `
'''
from datetime import datetime as pt
print(pt.now())
print(pt.year)
print('-----6-----datetime.datetime 模块'*5)

    # 7、OS模块 与操作系统相关
'''
    - 跟操作系统相关，主要是文件操作
    - 与系统相关的操作，主要包含在三个模块里
        os， 操作系统目录相关
        os.path, 系统路径相关操作
        shutil， 高级文件操作，目录树的操作，文件赋值，删除，移动
    - 路径：
        绝对路径： 总是从根目录上开始
        相对路径： 基本以当前环境为开始的一个相对的地方
'''
import os
    # -getcwd() 获取当前的工作目录
'''
格式：os.getcwd()
返回值：当前工作目录的字符串
当前工作目录就是程序在进行文件相关操作，默认查找文件的目录
'''
mydir = os.getcwd()
print(mydir)

    # -chdir() 改变当前的工作目录
'''
change directory
格式：os.chdir（路径）
返回值：无
os.chdir('/home/tlxy')
mydir = os.getcwd()
print(mydir)
'''

    # -listdir() 获取一个目录中所有子目录和文件的名称列表
'''
格式:os.listdir(路径)
返回值：所有子目录和文件名称的列表
'''
ld = os.listdir()
print(ld)

    # -makedirs()递归创建文件夹
'''
格式：os.makedirs(递归路径)
返回值：无 None
递归路径：多个文件夹层层包含的路径就是递归路径 例如 a/b/c...

ld1 = os.makedirs('dana')
print(ld1)
'''
    # -system()运行系统shell命令
'''
格式：os.system(系统命令)
返回值：打开一个shell或者终端界面
一般推荐使用subprocess代替

# ls 是列出当前文件和文件夹的系统命令
ld2 = os.system('ls')
print(ld2)

# 在当前目录下创建一个hahah 的文件
ld3 = os.system('touch hahah')
print(ld3)
'''

    # -getenv() 获取指定的系统环境变量值
'''
相应的还有putenv
格式：os.getenv('环境变量名')
返回值：指定环境变量名对应的值
'''
ld4 = os.getenv('PATH')
print(ld4)

    # exit() 退出当前程序
'''
格式：exit（）
返回值：无 
'''

    # 值部分
'''
os.curdir: curretn dir,当前目录
os.pardir: parent dir， 父亲目录
os.sep: 当前系统的路径分隔符
    windows: "\"
    linux: "/"
os.linesep: 当前系统的换行符号
    windows: "\r\n"
    unix,linux,macos: "\n"
os.name： 当前系统名称
    windows： nt
    mac，unix，linux： posix
'''
print(os.curdir)
print(os.pardir)
print(os.sep)
print(os.linesep)
print(os.name)
# 在路径相关的操作中，不要手动拼写地址，因为手动拼写的路径可能不具有移植性
path1  = '/home/tlxy' + '/' + 'dnna'
print(path1)
print('-----7-----OS 模块'*5)

    # 8、os.path 模块，跟路径相关的模块
import os.path as op
    # -abspath() 将路径转化为绝对路径
'''
abselute 绝对
格式:os.path.abspath('路径')
返回值：路径的绝对路径形式

-linux中
. 点号，代表当前目录
.. 双点，代表父目录
'''
abspath = op.abspath('.')
print(abspath)

    # -basename()获取路径中的文件名部分
'''
格式:os.path.basename(路径)
返回值：文件名字符串
'''
bn = op.basename('/home/tlxy/dnna')
print(bn)
bn1 = op.basename('/work/高级语法-包/P01.py')
print(bn1)

    # -join() 将多个路径拼合成一个路径
'''
格式：os.path.join(路径1，路径2....)
返回值：组合之后的新路径字符串
'''
bd ='/work/高级语法-包/dana/'
fn ='pinjielujin'
pjlj = op.join(bd,fn)
print(pjlj)

    # -split() 将路径切割为文件夹部分和当前文件部分
'''
格式:os.path.split（路径）
返回值：路径和文件名组成的元组
'''
sp = op.split('/work/高级语法-包/dana/pinjielujin')
print(sp)
sp1,sp2 =op.split('/work/高级语法-包/dana/pinjielujin')
print(sp1,sp2)

    # -isdir() 检测是否是目录
'''
格式：os.path.isdir(路径)
返回值：布尔值
'''
rst = op.isdir('/work/高级语法-包/dana/pinjielujin')
print(rst)

    # -exists() 检测文件或者目录是否存在
'''
格式：os.path.exists(路径)
返回值:布尔值
'''
ex = op.exists('/work/高级语法-包/dana/pinjielujin')
print(ex)