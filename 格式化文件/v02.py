# etree读取xml文档
import xml.etree.ElementTree

root = xml.etree.ElementTree.parse("student.xml")
print("利用getiterator访问：")
# root.getiterator() 得到相应的可迭代的node集合
nodes = root.getiterator()
for node in nodes:
    print("{0}---{1}".format(node.tag, node.text))

print("利用find和findall方法：")
# root.find() 查找指定node_name节点，返回一个node
ele_teacher = root.find("Teacher")
print(type(ele_teacher))
print("{0}---{1}".format(ele_teacher.tag, ele_teacher.text))

# root.findall() 返回多个node_name节点列表
ele_stus = root.findall("Student")
print(type(ele_stus))
for ele in ele_stus:
    print("{0}---{1}".format(ele.tag, ele.text))
    # ele.getiterator() 得到相应的可迭代的node集合
    for sub in ele.getiterator():
        # sub.attrib.keys() 是node的属性的字典内容的值
        if "Other" in sub.attrib.keys():
            print(sub.attrib['Other'])