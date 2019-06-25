# -*- cocoding:utf-8 -*-
# 一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等）;

with open("./test.txt","r",encoding="gbk")as f:
    lines=f.readlines()
    for line in  lines:
        name=".".join(line,"py")
        with open(name,"a")as file:
            file.write("#")