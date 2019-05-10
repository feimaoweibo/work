    # 写一个6位随机验证码程序（使用random模块),要求验证码中至少包含一个数字、一个小写字母、一个大写字母
import random
import string
# help(string)
code = [] # 验证码列表为空
code.append(random.choice(string.ascii_lowercase))# 保证验证码中有一个小写字母
code.append(random.choice(string.ascii_uppercase))# 保证验证码中有一个大写字母
code.append(random.choice(string.digits))         # 保证验证码中有一个数字
while len(code) < 6 :
    # 往验证码列表里添加元素，添加6个元素以后结束循环
    code.append(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits))
print(code)
# 便于使结果好看，使用 string + join() 方式 连接序列中元素后生成新的字符串格式
q_code = "".join(code)
'''
-Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
-join()方法语法：str.join(sequence)
-参数：sequence -- 要连接的元素序列
-返回值：返回通过指定字符连接序列中元素后生成的新字符串。
-例子:
    str = "-";
    seq = ("a", "b", "c"); # 字符串序列
    print(str.join( seq ));
    以上实例输出结果如下：a-b-c
'''
print(q_code)

    # 生成6位纯数字验证码
code1 = []
while len(code1) < 6:
    code1.append(random.choice(string.digits))
print(code1)
q_code1 = ''.join(code1)
print(q_code1)

    # 生成6位大写字母验证码
code2 = []
while len(code2) < 6:
    code2.append(random.choice(string.ascii_uppercase))
print(code2)
q_code2 = ''.join(code2)
print(q_code2)

    # 生成6位小写字母验证码
code3 = []
while len(code3) < 6:
    code3.append(random.choice(string.ascii_lowercase))
print(code3)
q_code3 = ''.join(code3)
print(q_code3)
