def fuc1(x):
    return x + x


def fuc2(x):
    return x * x * x


def demo(f):
    def f_new(x):
        print(f.__name__)
        return f(x)

    return f_new


t = demo(fuc1)
print(t(2))
# fuc1
# 4

r = demo(fuc2)
print(r(2))


# fuc2
# 8

@demo
def fuc3(x):
    return x * 2 * x


print(fuc3(3))

# fuc3
# 18
