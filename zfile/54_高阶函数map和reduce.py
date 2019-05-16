from functools import reduce

a = [1, 2, 3, 4, 5]

print([item for item in map(lambda x: x * x, a)])  # [1, 4, 9, 16, 25]

# 求5个数之和

# def f(x, y):
#     return x + y
b = reduce(lambda x, y: x + y, a)
print(b)
