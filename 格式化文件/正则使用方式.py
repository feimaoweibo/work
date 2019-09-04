# 一、RE正则表达式使用的大致步骤
'''
1、使用compilc将表示正则的字符串编译为一个pattern对象
2、通过pattern对象提供一系列方法对文本进行查找匹配，获得匹配结果，一个Match对象
3、最后使用Match对象提供的属性和方法获得信息，根据需要进行操作
'''
# 二、RE常用函数
'''
group() ：获得一个或者多个分组匹配的字符串，当要获得整个匹配的字符串时，直接使用group或者group(0)
start: 获得分组匹配的子串在整个字符串中的起始位置，参数默认为0
end: 获取分组匹配的子串在整个字符串中的结束位置，默认为0
span: 返回的结构技术（start（group）,end(group)）
'''
# 三、导入正则表达式模块
import re
# 案例代码1、
# 通过compile()函数把正则的字符串编译为pattern对象
# r:表示‘’内的字符串内容不转义，\d 表示数字，+表示至少出现1次
p = re.compile(r'\d+')
# 通过按照pattern对象提供指定的方法，在字符串one12twothree3456four78中进行查找
m = p.match("one12twothree3456four78")
# 返回结果是None表示没有找到，否则会返回match对象
print(m)
# match（）可以输入参数表示起始和结束位置，查找到的结果只包含一个，表示第一次进行匹配成功的内容
m1 = p.match("one12twothree3456four78", 3, 6)
print(m1)
print(m1[0])#m1[0] 表示第一个匹配结果
print(m1.start(0))#表示开始位置
print(m1.end(0))#表示结束位置
print("--------------1------------------")

# 案例代码2、
# re.I表示忽悠大小写
p = re.compile(r'([a-z]+) ([a-z]+)', re.I)#()表示分组，此正则表达式为分成2组同时中间有空格号，[]表示匹配中括号中a-z字符，+表示至少出现1次
m2 = p.match("I am really love wangxiaojing")
print(m2)
print(m2.group(0))# 表示获得整个匹配的字符串内容
print(m2[0])#表示匹配第一个结果
print(m2.start(0))
print(m2.end(0))

print(m2.group(1))# 表示获得第一个组的字符串内容
print(m2.start(1))# 表示第一个组的起始位置
print(m2.end(1))# 表示第一个组的结束位置
# groups()表示所有分组的字符串内容
print(m2.groups())
print("--------------2-----------------")

# 四、查找
'''
search(str,[,pos[,endpos]]):在字符串中查找匹配，pos和endpos表示起始位置，返回是match对象
findall:查找所有,返回的结果类型是列表
finditer:查找，返回一个iter（可迭代对象）结果
'''
# 案例代码3、
p = re.compile(r'\d+')
m3 = p.search("one12two34three567four")
print(m3)
print(m3.group(0))
# findall()在字符串中查找所有
m4 =p.findall("one12two34three567four")
print(type(m4))
print(m4)
print("----------------3--------------------")

# 五、匹配中文
'''
大部分中文内容表示范围是[u4e00-u9fa5]
不包括全角标点符
'''
# 案例代码4、
title = '世界 你好，hello world'
p = re.compile(r'[\u4e00-\u9fa5]+') #\u4e00 与 \u9fa5 表示中文范围
m5 = p.findall(title)
print(m5)
print("----------4-----------------------")

# 六、贪婪和非贪婪
'''
贪婪：尽可能多的匹配，（*）表示贪婪匹配
非贪婪：找到符合条件的最小内容即可，（？）表示非贪婪
正则默认使用贪婪模式匹配
在python的爬虫使用非贪婪模式
'''
tanlan = "<div>name</div><div>age</div>"
p = re.compile(r'<div>.*</div>')# 贪婪模式
m6 = p.search(tanlan)
print(m6.group(0))
p = re.compile(r'<div>.*?</div>')#非贪婪模式
m7 = p.search(tanlan)
print(m7.group(0))