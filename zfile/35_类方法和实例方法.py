class Users:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("my name is {}, I'm {}!".format(self.name, self.age))
        self.tes1()  # 可以调用本类中的类方法
        # self.tes2()   # 不能调用本类中的静态方法

    @classmethod
    def tes1(cls):
        print("test1是一个类方法")
        cls.test2()  # 可以调用本类中的静态方法
        # cls.hello() # 不能调用本类中的类方法

    @staticmethod
    def test2():  # 不能调用本类中的其他方法
        print("test2 是一个静态方法")


use = Users("jeck", 23)
use.hello()
use.tes1()
use.test2()
Users.tes1()  # 可以直接调用 @classmethod 类方法
Users.test2()  # 可以直接调用 @staticmethod 类方法
