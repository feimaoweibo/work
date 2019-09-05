# XPath概念
    在XML文件中查找信息的一套规则/语音，根据XML的元素或者属性进行遍历
    http://www.w3school.com.cn/xpath/index.asp
# XPath开发工具
    开源的XPath表达式编辑工具：XMLQuire
    Chrome插件：XPath Helper
    Firehox插件：XPath Checker
# 代码示例
<?xml version="1.0" encoding="utf-8" ?>
<School>
    <Teacher desc="PythonTeacher" score="good">
        <Name>Liudana</Name>
        <Age_1 Detail=" Age for year 2010">18</Age_1>
        <Mobile>13260446055</Mobile>
    </Teacher>
    <Student>
        <Name Other="他是班长">Zhangsan</Name>
        <Age Detail="The yongest boy in class">14</Age>
    </Student>
    <Student>
        <Name>Lisi</Name>
        <Age>19</Age>
        <Mobile>15588883333</Mobile>
    </Student>
    <!-- 这是注释的写法，双短横线格式写法 -->
</School>

# 选取节点操作
    ndoename：选取此节点的所有子节点
    / ：从根节点开始选取
        /Student ：没有结果
        /School ：选取School所有节点
    // ：选取节点，不考虑位置
        //age ：选取去2个节点，一般组成列表返回
    . ：选取当前节点    
    .. ：选取当前节点的父亲节点
    @ ：选取属性
    Xpath中查找一般按照路径方法查找，以下是路径表示方法
        School/Teacher：返回Teacher节点
        School/Stedent：返回两个Student的节点
        //Student：选取所有Student的节点，不考虑位置
        School//Age：选取School后代中所有的Age节点
        //@Other：选取Other属性
        //Age[@Detail]：选取带有属性Detail的Age元素（或者节点）
        
# 谓语-Predicates
    /School/Student[1]：选取School下面的第一个Student节点
    /School/Student[last()]：选取School下面的最后一个Student节点
    /School/Student[last()-1]：选取School下面的倒数第二个Student节点
    /School/Student[position()<3]：选取School下面的前二个Student节点
    //Student[@score]：选取带有属性score的Student节点
    //Student[@score="99"]：选取带有属性score并且属性值是99的Student节点
    //Student[@score]/Age：选取带有属性score的Student节点的子节点Age
    
# Xpath的运算符操作
    | ：表示 和 意思
        //Student[@score] | //Teacher：选取带有属性score的Student节点和Teacher节点
    其余不常见XPath运算符号包括 + , - , * , div, > , <
    
    
        
    
    
    
    
    
    
    
    


    



