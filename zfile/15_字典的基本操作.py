user = {
    'Name': 'Jack',
    'Age': 18,
    'sex': '男'
}
print(user.get('names'))  # None
print(user.keys())  # dict_keys(['Name', 'Age', 'sex'])
print(user.values())  # dict_values(['Jack', 18, '男'])
print(user.items())  # dict_items([('Name', 'Jack'), ('Age', 18), ('sex', '男')])

it = {
    1: 1,
    2: 2,
    3: 3
}
iq = it.pop(3)
print(iq)  # 3
print(it)  # {1: 1, 2: 2}
# it[4] = 4
# it[5] = 5
# print(it)  # {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

ie = {'a': 'a',
      'b': 'b'
      }
# 更新一
# it.update(ie)
# print(it)  # {1: 1, 2: 2, 'a': 'a', 'b': 'b'}
# 更新二
e = {**it, **ie}
print(e)  # {1: 1, 2: 2, 'a': 'a', 'b': 'b'}
