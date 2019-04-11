# 模块
# 1、模块
'''
- 一个模块就是一个包含Python代码的文件，后缀名是 .py 就可以，模块就是一个Python文件
- 为什么我们要用模块
    - 程序太大，编写维护非常不方便，需要拆分
    - 模块可以增加代码重复利用
    - 当做命名空间使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件
    - 根据模块的规范，最好在模块中编写以下内容
        - 函数（单一功能）
        - 类（相似功能的组合，或者类似业务模块）
        - 测试代码
- 如何使用模块
    - 模块直接导入
    - 语法
        import module_name
        module_name.function_name
        module_name.class_name
        - 案例 P01 、导入第一个模块案例
    - 模块名称以数字开头，需要借助importlib帮助
        - 语法
            - import importlib
            - bianliang = importlib.importlib_module('888数字开头模块')
        - 案例 数字开头模块案例、888数字开头模块
    - import 模块 as 别名
        - 导入的同时，给模块起一个别名
        - 语法与第一种相同
        - 案例 模块别名、 P01
    - from module_name import function_name,class_name
        - 此方法可以选择性导入 函数、类
        - 使用的时候可以直接使用导入内容，不需要前缀
        - 案例 模块内容选择性导入、 P01
    - from module_name import *
        - 导入模块所有内容（此方法会引起命名混淆）
        - 案例 模块所有内容导入、P01
    - if __name__ == '__main__': 的使用
        - 建议所有程序的入口都以此代码为入口
        - 可以有效避免模块代码被导入的时候被动执行的问题
'''

# 2、模块的所搜路径和存储
'''
    - 什么是模块的搜索路径
        - 加载模块的时候，系统会在哪些地方寻找此模块
    - 系统默认的模块搜索路径
        - 语法
            - import sys
            - sys.path 属性可以获取路径列表
            - 案例 模块搜索路径
    - 添加搜索路径
        - sys.path.append(dir)
    - 模块的加载顺序
        -1、搜索内存中已经加载好的模块
        -2、搜索Python的内置模块
        -3、搜索 sys.path路径
'''

# 包
'''
    - 包是一种组织管理代码的方式，包里面存放的模块
    - 用于将模块包含在一起的文件夹就是包
    - 自定义包的结构
        |---包
        |---|--- __init__.py  包的标志文件
        |---|--- 模块1
        |---|--- 模块2
        |---|--- 子包(子文件夹)
        |---|---|--- __init__.py  包的标志文件
        |---|---|--- 子包模块1
        |---|---|--- 子包模块2
    - 包的导入
        - import package_name
            - 直接导入一个包，可以使用__init__.py 中的内容
            - 使用方式
                package_name.function_name
                package_name.class_name.function_name()
            - 案例 pkg01、P03
        - import package_name as p
            - 具体用法跟作用方式，跟上述导入一致
            - 注意：此种方法是默认对__init__.py 内容的导入，慎用
        - import package.module
            - 导入包中某一个具体的模块
            - 使用方法
                package.module.function_name
                package.module.class.function()
                package.module.class.var
            - 案例  P04、pak01、p02
        - import package.module as pm
            - 导入包里模块时给模块起别名
            - 与模块起别名一样语法
        - from ... import ...导入
            - from package import module1\module2\module3......
            - 此种方法不执行 __init__.py 的内容
                from pkg01 import p02
                p02.sayHello()
'''