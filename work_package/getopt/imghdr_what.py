# -*- coding:utf-8 -*-
import imghdr

# imghdr.what，这个方法接受两个参数，第一个参数是一个文件对象，第二个参数是一个字节流数组。
# 文件对象用来对本地文件做检测；字节流用来对网络上的做检测

###判断图片类型
file1 = "F:\sc_all\打断点.jpg"
print(imghdr.what(file1))  # jpeg
file2 = "F:\sc_all\gfdsgfds.png"
print(imghdr.what(file2))  # png


###字节流判断图片类型---必须是"rb"权限
with open("F:\sc_all\打断点.jpg","rb")as file:  #jpeg
    print(imghdr.what(file))