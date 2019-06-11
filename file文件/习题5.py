'''
练习5、 编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在，
如果遇到文件夹，则进入该文件夹继续搜索
- input 去接受用户输入的文件名和开始搜索路径
- os.path.isdir() 函数判断文件是否是文件夹
- 循环调用函数
'''
import os
all_files = os.listdir(os.curdir)#接收当前路径下的所有文件
fname = input("请输入文件名： ")
start_dir = input("请输入查询路径： ")
def searchFile(fname, start_dir):
    os.chdir(start_dir)
    for each_file in all_files:
        if each_file == fname:
            print(os.getcwd() + os.sep + each_file)
        if os.path.isdir(each_file):
            searchFile(fname, start_dir)
            os.chdir(os.pardir)
searchFile(fname, start_dir)

