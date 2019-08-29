import xml.etree.ElementTree as et
# 在内存中创建一个空的文档
etree = et.ElementTree()
# 创建一个根元素
e = et.Element('Student')
# 设置子元素
etree._setroot(e)
e_name = et.SubElement(e, 'name')
e_name.text = 'hahahh'
etree.write('v06.xml')