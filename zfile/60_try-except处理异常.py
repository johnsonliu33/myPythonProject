a = [9, 4, 6, 11, 34, (1, 2, 3), 0, 5, 44, 21, 10]
try:
    b = [item for item in a if 100 % item == 0]
    print(b)
except ZeroDivisionError:
    print("0不能当做除数")
except TypeError:
    print("类型错误")
except Exception:
    print("其他错误")

print("==over==")
