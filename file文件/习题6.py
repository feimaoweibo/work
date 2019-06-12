'''
练习5、 编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在，如果遇到文件夹，则进入该文件夹继续搜索
 同时，我们需要保存我们的文件到指定路径的位置
- input 去接受用户输入的文件名和开始搜索路径
- os.path.isdir() 函数判断文件是否是文件夹
- 循环调用函数
- file 打开\写入
'''
import os
all_files = os.listdir(os.curdir) #接受当前路径下的所有文件
fname = input("请输入文件名： ")
start_dir = input("请输入搜索路径： ")
backup = [] #声明一个空的列表
def searchFile(fname, start_dir):
    os.chdir(start_dir)
    for each_file in all_files:
        if fname in each_file:
            backup_file = os.getcwd() + os.sep + each_file
            backup.append(backup_file)
        if os.path.isdir(each_file):
            searchFile(fname, start_dir)
            os.chdir(os.pardir)
    return backup
rd = searchFile(fname, start_dir) # 把函数的结果，赋值给rd
f = open(os.getcwd() + os.sep + "backup.txt", "wb")
f.write("\n".join(rd).encode("utf-8"))
f.close()