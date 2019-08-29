# python读取json文件案例
import json

data = {"name":"hahahh", "age":21}
# 以写入的方式，创建t.json文件
with open("t.json", 'w') as f:
    # 把内容data写入json格式的文件
    json.dump(data, f)
# 以只读的方式，打开t.json文件
with open("t.json", 'r') as f:
    # 把json格式的文件内容，读入python
    d = json.load(f)
    print(d)