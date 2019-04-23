se = {1, 2, 3, 4}
se.add(5)
se.add(5)
print(se)  # {1, 2, 3, 4, 5}
se.remove(5)  # {1, 2, 3, 4}
# se.remove(5)  # KeyError: 5

ss = 'abcdeabcde'
print(set(ss))  # {'b', 'd', 'a', 'c', 'e'}

s1 = {6, 7, 8, 9, 5}
s2 = {2, 5, 7, 0}
print(s1 & s2)  # {5, 7}
print(s1 | s2)  # {0, 2, 5, 6, 7, 8, 9}
print(s1 ^ s2)  # {0, 2, 6, 8, 9}
print(s1 - s2)  # {8, 9, 6}
print(s2 - s1)  # {0, 2}
