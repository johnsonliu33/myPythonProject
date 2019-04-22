# 字典的创建

a = {
    1: 'a',
    2: 'b',
    '3': 'c'
}
print(a, type(a))  # {1: 'a', 2: 'b', '3': 'c'} <class 'dict'>

# dict的key值必须是不可变的

b = (1, 2, 3)
c = {b: 'abc'}
print(c)  # {(1, 2, 3): 'abc'}

# e = [1, 2, 3]
# f = {e: 'qwe'}
# print(f)  # TypeError: unhashable type: 'list'

# 字典的访问
print(a[1])  # a
a[1] = 'h'
print(a[1])  # h
a[4] = 'add'
print(a)  # {1: 'h', 2: 'b', '3': 'c', 4: 'add'}
