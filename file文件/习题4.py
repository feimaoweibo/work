'''
练习4、 编写一个程序，计算当前文件夹下面所有文件的大小
- 打开文件
- 获取到所有文件及文件数据大小
- 保存获取的到数据，打印出来
'''
import os
all_files = os.listdir(os.curdir) #接收当前路径下的所有文件
file_dict = dict()#使用字典格式接收数据，即 文件名：数据大小
# for循环，遍历所有文件
for each_file in all_files:
    # os.path.isfile(path) 函数判断是否为文件
    if os.path.isfile(each_file):
        # os.path.getsize(path) 函数返回文件大小，如果文件不存在就返回错误
        file_size = os.path.getsize(each_file)
        file_dict[each_file] = file_size
for file in file_dict:
    print("{0}文件大小为{1}".format(file, file_dict[file]))
