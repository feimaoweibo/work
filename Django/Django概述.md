# Django框架 概述
    - 环境
        python3.7
        django1.8
    - 参考资料
        django中文教材：http://python.usyiyi.cn/
        django架站的16堂课
# 环境搭建
    - annconda + pycharm
    - annconda使用
        conda list: 显示当前环境安装的包
        conda env list: 显示安装的虚拟环境列表
        conda create -n env_name python=3.7
        激活conda的虚拟环境
            Linux：source activate env_name
            Win：activate env_name
        pip install django=1.8
# 创建第一个django程序
    - 命令行启动
        django-admin startproject tulingxueyuan
        cd tulingxueyuan
        python manage.py runserver
    - pycharm启动
        - 需要配置
# 路由系统-urls
    - 创建app
        app：负责一个具体业务或者一类具体业务的模块
        python manage.py startapp teacher
    - 路由
        按照具体的请求url，导入到相应的业务处理模块的功能
        django的信息控制中枢
        在本质上接受的URL和相应的处理模块的一个映射
        在接受URL请求的匹配上使用RE（正则表达式）
        URL的具体格式在urls.py中所示