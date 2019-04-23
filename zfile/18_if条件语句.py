### if
a = 12
if a > 10:
    print("a-小于10")
if a < 10:
    print("a-大于10")
# 输出 a-小于10


### if...else...

b = 10
if b > 10:
    print("b==小于10")
if b < 10:
    print("b==大于10")
else:
    print("b==都不是")
# 输出 b==都不是


### if ...elif...else...
for c in range(8, 13):
    if c > 10:
        print("c===小于10")
    elif c < 10:
        print("c===大于10")
    else:
        print("c===都不是")

# 输出
# c===大于10
# c===大于10
# c===都不是
# c===小于10
# c===小于10
