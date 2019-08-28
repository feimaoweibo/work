# xml文档的写入，生成创建案例
import xml.etree.ElementTree as et
stu = et.Element("Student1.xml")
name = et.SubElement(stu, 'Name')
name.attrib = {'lang', 'en'}
name.text = 'maozedong'

age = et.SubElement(stu, 'Age')
age.text = 18

et.dump(stu)