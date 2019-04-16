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