# -*- coding:utf-8-*-
# 高阶函数：函数可以被当做参数传递给另一个函数

param_list = [1, 2, 3]


def sum(param_list):
    return param_list[0] + param_list[1] + param_list[2]


def demo_test(param_list, sum):
    if type(param_list) is list:
        return sum(param_list)


print(demo_test(param_list, sum))  # 6
