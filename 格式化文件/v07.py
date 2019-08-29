# josn和python对象转换案例
import json
# 此时student是个dict格式的内容，不是json格式
student = {
    "name": "liudana",
    "age": 18,
    "mobile": "15322221111"
}
print(type(student))
print("--------11111-----------------")
# json.dumps():对数据编码，把python格式表示成json格式
stu_json = json.dumps(student)
print(type(stu_json))
print("JSON对象：{0}".format(stu_json))
print("--------2222------------------")
# json.loads(): 对数据解码，把json格式转换成python格式
stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)