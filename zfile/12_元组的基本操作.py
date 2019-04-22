tuple1 = (4, 7, -3, 9, 2, 4, 7, 0, 4, 5)
print("len : {}".format(len(tuple1)))  # len : 10
print("max : {}".format(max(tuple1)))  # max : 9
print("min : {}".format(min(tuple1)))  # min : -3
print("count : {}".format(tuple1.count(4)))  # count : 2

# 元组不能修改
# 元组不能翻转
# 元组不能排序

# index()查找参数在元组中的位置
print(tuple1.index(9))  # 3
