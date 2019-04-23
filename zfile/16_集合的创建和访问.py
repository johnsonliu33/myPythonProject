a = {1, 2, 3, 4, 'c'}
e = 'c' in a
print(e)  # True
f = 5 in a
print(f)  # False

# 利于set去重
L1 = [1, 2, 3, 2, 1, 's', 's']
s = set(L1)
print(s, type(s))  # {1, 2, 3, 's'} <class 'set'>
L2 = list(s)
print(L2, type(L2))  # [1, 2, 3, 's'] <class 'list'>
