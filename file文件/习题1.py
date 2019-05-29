'''
习题1、
编写一个程序，接受用户输入的内容，并且保存为新的文件
如果用户单独输入 :w表示文件保存退出
'''


#fileName = input('请输入文件名：')
def fileWrite(fileName):
    with open(fileName, 'w') as f:
        print('请输入内容（如果输入 tui 即保存退出）：')
        while True:
            neirong = input()
            # 判断用户输入的内容是不是 tui
            if neirong != 'tui':
                '''
                Python中关于 “%s”%str的用法：
                -一种字符串格式化的语法，基本用法是将值插入到 %s 占位符的字符串中
                %s ：表示占位符
                %str ：表示希望被格式化的值
                例子：string = "good"  #类型为字符串
                      print("string=%s" %string)   #输出的打印结果为 string=good  
                '''
                f.write('%s \n' %neirong)
            else:
                # 用户输入的 tui
                break
#fileWrite(fileName)



'''
习题2、
编写一个程序，比较用户输入的文件是否相同，如果不同，显示出所有不同处的行号
'''
file1 = input('请输入需要比较的第一个文件名： ')
file2 = input('请输入需要比较的第二个文件名： ')
def fileComare(file1, file2):
    count = 1
    differ = []

    with open(file1, 'r') as f:
        f1 = f.readline()
    with open(file2, 'r') as f:
        f2 = f.readline()
    for line1 in f1:
          if line1 != f2:
              differ.append(count)
          count +=1
    '''
    f1 = open(file1)
    f2 = open(file2)
    for line1 in f1:
        line2 = f2.readline()
        if line1 != line2:  # 文件不同
            differ.append(count)
        count += 1
    f1.close()
    f2.close()
    '''
    return differ
differ = fileComare(file1,file2)

if len(differ) == 0:
    print('两个文件完全相同')
else:
    print('两个文件有 %d 不同 '%len(differ))
    for each in differ:
        print('第%d行不一样'%each)
