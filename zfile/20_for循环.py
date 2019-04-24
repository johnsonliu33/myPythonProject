list1 = [1, 3, 5, 6]
for x in list1:
    print("list:{}".format(x))
    # list:1
    # list:3
    # list:5
    # list:6

tuple1 = (2, 4, 6, 8)
for t in tuple1:
    print("tuple:{}".format(t))
    # tuple:2
    # tuple:4
    # tuple:6
    # tuple:8

dict1 = {11: 11, 22: 22, 33: 33}
for d in dict1:
    print("dict:{}".format(d))
    # dict:11
    # dict:22
    # dict:33

for a, b in dict1.items():
    print("{}={}".format(a, b))
    # 11 = 11
    # 22 = 22
    # 33 = 33

set1 = {10, 20, 30, 40}
for s in set1:
    print("set:{}".format(s))
    # set:40
    # set:10
    # set:20
    # set:30
