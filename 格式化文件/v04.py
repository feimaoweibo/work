# xml文档的生成创建案例
import xml.etree.ElementTree as et
# 创建一个名叫 Stundent2的根元素
stu = et.Element("Student2")
# 创建一个子元素
name = et.SubElement(stu, 'Name')
name.attrib = {'lang', 'en'}
name.text = 'maozedong'
# 创建一个子元素
age = et.SubElement(stu, 'Age')
age.text = 18
# 提交
et.dump(stu)