def demo(s):
    def demo_new(f):
        def f_new(*args, **kwargs):
            print(s)
            print(f.__name__)
            return f(*args, **kwargs)

        return f_new

    return demo_new


@demo("hello world")
def demo_test(x, y, z):
    print("x={}, y={}, z={}".format(x, y, z))


demo_test(1, 3, 5)
"""
hello world
demo_test
x=1, y=3, z=5
"""
# 个人理解：
# 在函数上加个装饰器，并不会影响该函数，装饰器可以看做一个单独的函数，只不过在运行demo_test函数前要先运行demo函数
