'''
 练习1、
 编写一个程序，当用户输入文件名和行数的时候，将该文件的前N行内容打印到屏幕上
'''

viewName = input('请输入需要查询的文件名： ')
viewNum = input('请输入需要查询前N行： ')
def dayin(viewName, viewNum):
    print('需要查询的 %s 文件前 %s 的内容如下： '%(viewName, viewNum))
    with open(viewName, 'r') as f:
        for i in range(int(viewNum)):
            print(f.readline())
dayin(viewName, viewNum)


'''
练习2、
我们在上一道题的基础上，增加一点功能，使用户可以随意的输入需要显示的行数
[12:42]
[:]
用以上的形式来表示我们想要打印的起始和结束的行数
'''
fName = input('请输入需要查询的文件名： ')
lineNum = input('请输入你想要显示的起始行数如[2;8]或者[:]格式 ：')
def linePrint(fName, lineNum):
    f = open(fName)
    '''
    Python中的split()函数的用法
        通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）,同时可以赋值给新变量
        语法：str.split（str=' ', num=次数）[n]
        参数说明：
            str:表示为分隔符，默认为空格，但是不能为空('')。若字符串中没有分隔符，则把整个字符串作为列表的一个元素
                例如：s.split('')是不合法的表达
        num:表示分割次数。如果存在参数num，则仅分隔成 num+1 个子字符串，并且每一个子字符串可以赋给新的变量
        [n]:表示选取第n个分片
        例子：https://blog.csdn.net/qq_24407657/article/details/80265217
    '''
    begin, end = lineNum.split(':') # 此函数的作用：把lineNum字符串按“:”进行分割，并赋值给变量begin,end
    if begin == '':
        begin = '1'
    if end == '':
        end = '-1'
    begin = int(begin) - 1
    end = int(end)
    lines = end - begin # 表示打印的行数
    # 消耗点begin之前的行数
    for i in range(begin):
        f.readline()
    if lines < 0 :
        print(f.read())
    else:
        for j in range(lines):
            print(f.readline())
    f.close()
linePrint(fName, lineNum)
