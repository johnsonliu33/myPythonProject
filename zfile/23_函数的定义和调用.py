def demo():
    print("hello world")


demo()  # hello world


def demo1(a, b):
    print(a + b)


demo1(1, 2)  # 3
demo1("a", "b")  # ab


def my_max(a):
    if not a:
        return None
    max_value = a[0]
    for temp in a:
        if temp > max_value:
            max_value = temp
    print(max_value)


my_max([2, 7, 4, 6, 3, 9, 0])  # 9
my_max((2, 7, 14, 6, 3, 9, 0))  # 14
