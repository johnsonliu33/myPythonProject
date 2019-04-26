def fun(a, b=False):
    if b:
        return a
    else:
        return a * 2


print(fun(a=3, b=True))  # 3
print(fun(a="song"))  # songsong
