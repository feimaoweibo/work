# 一、结构化文件存储
'''
为了解决不同设备之间信息交换，提供2种解决文件方式
xml与json
'''
# 二、XML文件
'''
1、参考资料：
    https://docs.python.org/3/library/xml.etree.elementtree.html
    http://www.runoob.com/python/python-xml.html
    https://blog.csdn.net/seetheworld518/article/details/49535285
2、XML（eXtensibleMarkupLanguage），可扩展标记语音
    标记语言：语言中使用尖括号<>样式括起来的文本字符串标记
    可扩展：用户可以自己定义需要的标记
    例如：
        <Teacher>
            自定义标记Teacher
            在两个标记之间任何内容都应该跟Teacher相关
        </Teacher>
    是W3C组织制定的一个标准
    XML描述的数据本身，即数据的结构和语义
    HTML侧重于如何显示WEB页面中的数据
3、XML文档的构成
    处理指令（可以认为一个文件内只有一个处理指令）
        最多只有一行
        且必须在第一行
        内容是与xml本身处理起相关的一些声明或者指令
        以xml关键字开头
        一般用于声明XML的版本和采用编码格式
            ersion属性是必须的
            encoding属性用来指出xml解释器使用编码的格式
    根元素（一个文件内只有一个根元素）
        在整个xml文件中，可以把他看作一个树形结构
        根元素有且只能有一个
    子元素
    属性
    内容
        表明标签所存储的的信息
    注释
        起说明作用的信息
        注释不能嵌套在标签里
        只有在注释的开始和结尾使用双短横线
        三短横线只能出现在注释的开头而不能用在结尾
            <name><!-- wangdapeng --></name>  # 可以
            <name <!-- wangdapeng -->></name> # 不可以，注释在标签内
            <!--my-name-by-wang--> #可以，注释内容可以有一个短横线
            <!--my--name--by--wang--> #不可以，双短横线只能出现在开头或结尾
            <!---my-name--> #可以，三短横线只能出现在开头
            <!---my-name--->#不可以，三短横线只能出现在开头
4、保留字符的处理
    XML中使用的符号可能跟实际符号相冲突，典型的就是左右尖括号
    使用实体引用（EntityReference）来表示保留字符
        <score> score>80 </score> #有错误，xml中不能出现>
        <score> score&gt;80 </score> #使用实体引用
    把含有保留字符的部分放在CDATA块内部，CDATA块把内部信息视为不需要转义
        <![CDATA[
            select name, age
            from Student
            where score>80
            ]]>
    常用的需要转移保留字符和对应实体引用表(一共5个，每个实体引用都以&开头并且以分号结尾)
        & ：&amp;
        < ：&lt;
        > ：&gt;
        ' ：&apos;
        " ：&quot;
        
'''