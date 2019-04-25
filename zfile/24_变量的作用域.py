x = 1
x += 1
print(x)  # 2


def fun1():  # 函数内不会修改函数外的参数值
    x = 10
    print(x)  # 10


fun1()
print(x)  # 2


def fun2():  # 使用global，函数内会修改函数外的参数值
    global x
    x = 10
    print(x)  # 10


fun2()
print(x)  # 10

list2 = [1, 2, 3]


def demo(loc):  # loc = 会重新定义一个参数，不会修改传入的参数
    loc = loc + [4]
    print(loc)  # [1, 2, 3, 4]


demo(list2)
print(list2)  # [1, 2, 3]


def demo2(loc):  # append()会修改会修改传入的参数
    loc.append(4)
    print(loc)  # [1, 2, 3, 4]


demo2(loc=list2)
print(list2)  # [1, 2, 3, 4]
