#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import time


# 可写函数说明
def printinfo(arg1, *vartuple):
    """打印任何传入的参数"""
    print('输出: ')
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
total = sum(10, 20)
print("函数内 : ", total)

Money = 2000


def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1


print(Money)
AddMoney()
print(Money)

# 打开一个文件
fo = open("ttttt.txt", "w")
print("文件名: ", fo.name)
fo.write("1fjdkgfdsaggfdsgfdsgfdsgfdsgfs2lafjgfdsgfdsggfdsgfdsfdsgfdsdsa3")

fo = open("ttttt.txt", "r")
str = fo.read(22)
print("访问模式 : ", str)
fo.close()
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)

# print ("末尾是否强制加空格 : ", fo.softspace)




localtime = time.localtime(time.time())
print("本地:", localtime)
print(time.clock())

# 打开一个文件
fo = open("ttttt.txt", "r+")
str = fo.read(20)
print("读取的字符串是 : ", str)

# 查找当前位置
position = fo.tell()
print("当前文件位置 : ", position)
str = fo.read(5)
print("当前文件位置  : ", str)

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(100)
print("重新读取字符串 : ", str)
# 关闭打开的文件
fo.close()
