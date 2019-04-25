def my_add(*args):
    result = 0
    for temp in args:
        result = result + temp
    return result


sum = my_add(1, 2, 3, 4, 5)
print(sum)  # 15
