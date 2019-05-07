# isinstance() 与 type() 区别：
#   type() 不会认为子类是一种父类类型，不考虑继承关系。
#   isinstance() 会认为子类是一种父类类型，考虑继承关系。
# 如果要判断两个类型是否相同推荐使用 isinstance()。

a = [1, 2]
print(type(a))  # <class 'list'>
c = 12
print(isinstance(c, int))  # True
print(isinstance(c, str))  # False
print(isinstance(c, (int, str, list)))  # True


class F:
    pass


class H(F):
    pass


print(isinstance(F(), F))  # True
print(isinstance(H(), F))  # True
print(type(F) == type(H))  # True
print(type(F()) == F)  # True
print(type(H()) == F)  # False
