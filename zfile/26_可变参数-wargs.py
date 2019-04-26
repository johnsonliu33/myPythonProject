def fun(**kwargs):
    print(kwargs)  # {'a': 1, 'b': 2, 'c': 3}
    return (kwargs.get("a") + kwargs.get("b")) * kwargs.get("c")


print(fun(a=1, b=2, c=3))  # 9


def add(a, b, c):
    return a + b + c


def fun2(x, **kwargs):
    if x == 2:
        return add(**kwargs)


print(fun2(x=2, a=1, b=2, c=3))  # 6
