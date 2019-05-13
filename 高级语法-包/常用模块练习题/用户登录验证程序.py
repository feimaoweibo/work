    # 写一个用户登录验证程序，文件如下 1234.json
'''
1234.json
{"expire_date":"2021-01-01","id":"1234","status":0,"pay_day":22,"password":"abc"}

    用户名为json的文件名
    判断是否过期，与expire_date做比较
    登陆成功后打印登陆成功，三次登陆失败，status值改为1，并且锁定账号
'''
import os
import time
import json
# help(json)
count = 0 # 声明次数
exit_flag = False # 声明是否退出，默认否
while count < 3:
    user = input('请输入用户名：')
    f = user.strip() + '.json' # 创建以用户名命名的json文件，使用字符串拼接形式: 以 .strip() 清除用户名前后的空格，加上字符串'.json'，形成json文件
    # 判断通过用户输入用户名组成的json格式的文件f 是否存在
    if os.path.exists(f):
        fp = open(f,'r+',encoding='utf-8') # open(path, ‘-模式-‘,encoding=’UTF-8’) 即open(路径+文件名, 读写模式, 编码)，并打开
        j_user = json.load(fp) # 获取以json数据类型读取的fp文件属性
        if j_user['status'] == 1: # 判断fp文件里的 ‘status’属性值，是否为1
            print('账号已经被锁定')
            break
        else:
            expire_dt = j_user['expire_date'] # 获取 fp文件里的‘expire_date’属性：到期时间
            current_st = time.time() # 获取当前时间戳
            expire_st = time.mktime(time.strptime(expire_dt,'%Y-%m-%d')) # 获取到期时间戳，使用time.mktime()方式，通过time.strptime()将fp文件里的到期时间属性，转化为自定义为年-月-日格式，
            # 判断当前时间戳 大于 到期时间戳
            if current_st > expire_st:
                print('用户已经过期')
                break
            # 没有到到期时间
            else:
                # while循环，输入密码只能3次
                while count < 3:
                    pwd = input('请输入密码：')
                    # 使用.strip()方式来清除密码首尾的空字符串得到密码，是否等于fp文件里面‘password’属性的值
                    if pwd.strip() == j_user['password']:
                        print('登录成功')
                        exit_flag = True # 退出登录
                    # 密码不相同，则判断
                    else:
                        # 如果密码已经输入三次
                        if count ==2:
                            print('用户输出密码已经超过3次，账号被锁定')
                            j_user['status'] = 1 # fp文件的‘status’属性赋值为1
                            fp.seek(0) # file.seek()方法用于移动文件读取指针到指定位置,0表示从文件开头开始
                            fp.truncate() # file.truncate()方法用于截断文件，从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断
                            json.dump(j_user,fp) # 以 json格式存储fp文件
                    # 输入密码次数自增1
                    count +=1

    # 组成同名的json格式文件，不存在
    else:
        print('用户不存在')
        count += 1

'''
    -str.strip()描述
        Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
        注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
    -语法
        strip()方法语法：str.strip([chars]);
    -参数
        chars -- 移除字符串头尾指定的字符序列。
    -返回值
        返回移除字符串头尾指定的字符生成的新字符串。
    -实例
        以下实例展示了strip()函数的使用方法：
            str = "00000003210Runoob01230000000"; 
            print str.strip( '0' );  # 去除首尾字符 0
            打印结果：3210Runoob0123
    
            str2 = "   Runoob      ";   # 去除首尾空格
            print str2.strip();
            打印结果：Runoob
    
            str = "123abcrunoob321"
            print (str.strip( '12' ))  # 字符序列为 12
            打印结果：3abcrunoob3
'''

'''
- open(path, ‘-模式-‘,encoding=’UTF-8’) 即open(路径+文件名, 读写模式, 编码)
- 在python对文件进行读写操作的时候，常常涉及到“读写模式”，整理了一下常见的几种模式，如下：
    读写模式：
        r ：只读 
        r+ : 读写 
        w ： 新建（会对原有文件进行覆盖） 
        a ： 追加 
        b ： 二进制文件
- 常用的模式有：
    “a” 以“追加”模式打开， (从 EOF 开始, 必要时创建新文件) 
    “a+” 以”读写”模式打开 
    “ab” 以”二进制 追加”模式打开 
    “ab+” 以”二进制 读写”模式打开
    
    “w” 以”写”的方式打开 
    “w+” 以“读写”模式打开 
    “wb” 以“二进制 写”模式打开 
    “wb+” 以“二进制 读写”模式打开
    
    “r+” 以”读写”模式打开 
    “rb” 以”二进制 读”模式打开 
    “rb+” 以”二进制 读写”模式打开
    
    rU 或 Ua 以”读”方式打开, 同时提供通用换行符支持 (PEP 278)

- 需注意：
    1、使用“w”模式。文件若存在，首先要清空，然后重新创建 
    2、使用“a”模式。把所有要写入文件的数据都追加到文件的末尾，即使你使用了seek（）指向文件的其他地方，如果文件不存在，将自动被创建。    
    3、f.read([size]) ：size未指定则返回整个文件，如果文件大小>2倍内存则有问题。f.read()读到文件尾时返回”“(空字串) 
    4、file.readline() 返回一行 
    5、file.readline([size]) 返回包含size行的列表,size 未指定则返回全部行 
    6、”for line in f: print line” #通过迭代器访问 
    7、f.write(“hello\n”) #如果要写入字符串以外的数据,先将他转换为字符串. 
    8、f.tell() 返回一个整数,表示当前文件指针的位置(就是到文件头的比特数). 
    9、f.seek(偏移量,[起始位置]) ： 用来移动文件指针 
    偏移量 : 单位“比特”,可正可负 
    起始位置 : 0 -文件头, 默认值; 1 -当前位置; 2 -文件尾 
    10、f.close() 关闭文件
'''

'''
- seek()方法用于移动文件读取指针到指定位置。
    file.seek()方法标准格式是：file.seek(offset,whence)
    offset：开始的偏移量，也就是代表需要移动偏移的字节数
    whence：给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。whence值为空没设置时会默认为0。
'''