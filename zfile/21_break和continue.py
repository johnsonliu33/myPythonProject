# break

for i in range(1, 10):
    if i % 2 == 0:
        # print("break:{}".format(i))   # 2
        break
    print("break:{}".format(i))  # 1
# continue
for j in range(10, 20):
    if j % 2 == 0:
        # print("continue:{}".format(j)) # 10, 12, 14, 16, 18
        continue
    print("continue:{}".format(j))  # 11, 13, 15, 17, 19
# 猜数字游戏，直到猜对为止
while True:
    temp = int(input("请输入一个数字："))
    if temp == 10:
        print("恭喜你猜对了！")
        break
    else:
        print("猜错了，继续猜吧。。。")
        continue
