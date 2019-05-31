'''
 练习1、
 编写一个程序，统计当前目录下每个文件类型的个数
 思路：
    打开当前的文件夹
    获取当前文件夹下面所有的文件（会出现子文件夹）
    做出统计
'''
import os
all_files = os.listdir(os.curdir)
type_dict = dict()
for each_file in all_files:
    '''
    Python编程语言判断是否是目录
        在Python编程语言中可以使用os.path.isdir()函数判断某一路径是否为目录。其函数原型如下所示。
        os.path.isdir(path) 
        其参数含义如下。path 要进行判断的路径。以下实例判断E:\book\temp是否为目录。
            >>> import os  
            >>> os.path.isdir('E:\\book\\temp')     
            True  表示 E:\book\temp是目录
    Python编程语言判断是否为文件
        在Python编程语言中可以使用os.path.isfile()函数判断某一路径是否为文件。其函数原型如下所示。
        os.path.isfile(path) 
        其参数含义如下。 path：要进行判断的路径。以下实例判断E:\book\temp是否为文件。
            import os 
            os.path.isfile('E:\\book\\temp')   
            False 
    '''
    if os.path.isdir(each_file):
        '''
        Python 字典(Dictionary) setdefault()方法
            描述
                Python 字典 setdefault() 函数和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
            语法
                setdefault() 方法语法：
                dict.setdefault(key, default=None)
            参数
                key -- 查找的键值。
                default -- 键不存在时，设置的默认键值。
            返回值
                如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值。
        '''
        type_dict.setdefault("文件夹", 0)
        type_dict["文件夹"] += 1
    else:
        ext = os.path.splitext(each_file)[1]
        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1
for each_type in type_dict:
    print("该文件夹下面有类型为{}的文件{}个".format(each_type, type_dict[each_type]))
