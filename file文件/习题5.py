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
    # 切换到用户输入的路径
    os.chdir(start_dir)
    for each_file in all_files:
        if each_file == fname:
            # os.getcwd()返回当前工作目录；os.sep跨平台解决文件的路径分隔符\ 与 /书写问题；
            print(os.getcwd() + os.sep + each_file)
        '''
        - 对上述题目加一些需求，模糊匹配，判断我们的fname是否包含在某一个文件中
        - 使用if...in...判断fname这个字符串是否在文件名字中
        '''
        if fname in each_file:
            print(os.getcwd() + os.sep + each_file)
        if os.path.isdir(each_file):
            searchFile(fname, start_dir)
            os.chdir(os.pardir)#os.pardir获取当前目录的父目录字符串，
searchFile(fname, start_dir)


