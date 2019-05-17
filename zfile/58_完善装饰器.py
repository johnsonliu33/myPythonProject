import functools


def demo(f):
    @functools.wraps(f)
    def f_new(*args, **kwargs):
        """
        this is f_new
        :param args:
        :param kwargs:
        :return:
        """
        print(f.__name__)  # demo_test
        return f(*args, **kwargs)

    return f_new


@demo
def demo_test(x, y, z):
    """
    this is demo_test
    :param x:
    :param y:
    :param z:
    :return:
    """
    print("x={}, y={}, z={}".format(x, y, z))


demo_test(1, 3, 5)
print(demo_test.__name__)  # demo_test
print(demo_test.__doc__)
# this is demo_test
# :param x:
# :param y:
# :param z:
# :return:
