a = [1, 2, 3, 4, 5]
# a = filter(lambda x: x % 2 == 1, a)
print([item for item in filter(lambda x: x % 2 == 1, a)])  # [1, 3, 5]
print([item for item in a if item % 2 == 1])  # [1, 3, 5]
