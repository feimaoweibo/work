# 1、利用map()函数，把用户输入的不规范的英文，变成首字母大写，其他小写的规范的名字：
# 比如说["ADMAm","LISA","JACk"] ---->["Admam","Lisa","Jack"]
def standstrs(s):
    '''
    str.lower() : 将字符串全部小写函数
    str.capitalisz() : 将字符串首字母大写函数
    '''
    t = s.lower()  # 第一步 传入参数s,并将参数s的字符串内容，全部小写，再赋值给变量t
    t = t.capitalize() # 第二步 将变量t 的字符串内容 首字母大写后，再重新赋值给变量t
    return t # 第三步 standstrs函数结果是返回 变量t
# 方案1、使用map()函数，直接写入列表内容
l1 = map(standstrs,["ADMAm","LISA","JACk"] )
l2 = [i for i in l1] # 使用列表生成式，方便打印列表内容明细
print(l2)
# 方案2、 声明列表变量，使用map()函数时，直接使用变量列表名
l3 = ["ADMAm","LISA","JACk"]
l4 = map(standstrs,l3)
print([e for e in l4]) # 直接打印列表生成式的内容
# 方案3、使用匿名函数 lambda表达式
l5 = map(lambda x: x.lower().capitalize(), l3)
print(l5)
print(list(l5))
print('----- map()映射函数'*5)


# 2、请利用filter()函数
# 回数：从左向右和从右向左读都是一样的数，例如 12321，999，
# 方案1
def equal(a,b): # 声明一个值相等的函数
    return a==b
def isPan(n): # 声明判断角标上值是否相等的过滤函数
    s = str(n) # 先把数字转换成字符串
    # 用for循环遍历字符串里所有位置上的数值
    for i in range(len(s)-1): # len(s)-1 表示：len(s)表示字符串的长度，由索引值来绑定位数，因此len(s)-1即为最后一位
        # 判断对应的值是否相等，相同则继续
        if equal(s[i],s[len(s)-i-1]):# s[i]表示字符串索引值对应位数上的值，len(s)-i-1表示与i相对位置
            continue
        # 不等则返回 假
        else:
            return False
    # isPan函数返回值为真
    return True
num = filter(isPan,range(1,10000)) # 使用filter()函数过滤数据，返回满足条件而返回的布尔值
num1 = [i for i in num] # 使用列表生成式来接受返回的布尔值列表
print('1-10000回数集合：',num1)
# 方案2、使用匿名函数 lanbda()表达式
lne = range(1000)
lnee   = filter(lambda x: str(x)[0] == str(x)[len(str(x))-1], lne)# 此表达式只能展示999以内的回数,str(x)[0]表示首位数字，str(x)[len(str(x))-1]表示末尾数字
print(list(lnee))
print('-----filter()过滤函数'*5)

# 3、请利用sorted()函数排序
# 假设，我们用一组tuple来表示学生的名字和成绩，L = [("Bob",75),("Adam",92),("Bart",66),("List",88)]
L = [("Bob",75),("Adam",92),("Bart",66),("List",88)]
    # 使用字母排序 ，a-->z
# 方案1、
def byName(t):
    t = sorted(t[0],key=str.lower) # t[0] 表示元组第一个值，str.lower表示字符串小写
    return t
name = sorted(L,key=byName)
print(name)
# 方案2、使用匿名函数 lambdaz()表达式
nameL = sorted(L, key=lambda x: x[0], reverse=False)
print(list(nameL))

    # 使用分数高低排序
# 方案1、
def byScore(t):
    t = sorted(range(t[1]),key=abs)
    return t
name1 = sorted(L,key=byScore,reverse=True)
print(name1)
# 方案2、使用匿名函数 lambda()表达式
name1L = sorted(L, key=lambda x:x[1],reverse=True)
print(list(name1L))

