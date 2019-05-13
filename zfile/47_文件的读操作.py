f = open("test.txt", "r")  # f 是迭代器，不会存入缓存，只能读取一遍
print(f.read())  # 一次读取全部内容
for line in f:
    print(line)  # 一次读取一行内容
print(f.readline())  # 一次读取一行内容
print(f.readlines())  # 一次读取全部内容
f.seek(0)  # 光标移动到0的位置
