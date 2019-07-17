# lambda匿名函数


# 不使用lambda
def lamb(x, y):
    return x + y


def lamb2(x, y, lamb):
    return lamb(x, y)


print(lamb2(1, 2, lamb))  # 3


# 使用lambda
def lamb3(x, y, f):
    return f(x, y)


print(lamb3(1, 2, lambda x, y: x + y))  # 3


#
def add_n(n):
    print("n=%d" % n)  # n=10
    return lambda x: n + x


f = add_n(10)  # 调用f函数时，传输参数x=1,f函数再调用add_n函数，传入参数n=10
print(f(1))  # 11
print(f(-20))  # -10


# 与map/filter/reduce的联合使用
# 使用lambda定义的匿名函数可与Python提供的map、filter、reduce等全局函数结合使用，其示例如下所示：
#
# >>> list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> map(lambda x: x * 2, list)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# >>> filter(lambda x: x % 3 == 0, list)
# [3, 6, 9]
# >>> reduce(lambda x, y: x + y, list)
# 55