# -*- coding:utf-8 -*-

from xml.dom import minidom

# 打开文件
dom = minidom.parse("test.xml")
# 获取对象元素
root = dom.documentElement
#############################
#############################
# 读取节点信息
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)  # 如果节点是元素节点，返回1；如果节点是属性节点，返回2
#############################
#############################
# 读取子节点信息
tags = root.getElementsByTagName('student')
print(tags[0].nodeName)
print(tags[0].tagName)
print(tags[0].nodeType)
print(tags[0].nodeValue)
#############################
#############################
# 读取节点内容
names = root.getElementsByTagName("name")
ages = root.getElementsByTagName("age")
citys = root.getElementsByTagName("city")
for i in range(len(names)):
    print(names[i].firstChild.data)
    print(ages[i].firstChild.data)
    print(citys[i].firstChild.data)
#############################
#############################
# 读取属性内容
logins = root.getElementsByTagName("login")
# 获取login标签的username属性
for j in range(len(logins)):
    print(logins[j].getAttribute("username"))
    print(logins[j].getAttribute("password"))
