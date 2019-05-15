a = [1, 2, 3, 4, 5, 6]
# 解析集合
b = [item for item in a]
print(b)  # [1, 2, 3, 4, 5, 6]
# 解析集合并计算
c = [item * item for item in a]
print(c)  # [1, 4, 9, 16, 25, 36]
# 遍历集合中的偶数
d = [item for item in a if item % 2 == 0]
print(d)  # [2, 4, 6]
print(5 / 2)  # 2.5  求商
print(5 % 2)  # 1  取余
