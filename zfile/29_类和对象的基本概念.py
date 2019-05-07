# class 是一个抽象的集合
# 对象 是一个真是存在的实例

def fun():  # function(函數)
    pass


class ClassName():  # class(类)
    def __init__(self, name, age):  # method(方法)
        self.name = name  # attribute(属性)
        self.age = age  # attribute(属性)

    def meth(self):  # method(方法)
        print("my name is : {},  age is : {} ".format(self.name, self.age))


somebody = ClassName(name="python", age=15)
somebody.meth()

print("***class外部可以直接访问ClassName类中的公共属性name***：{}".format(somebody.name))
somebody.name = "black"
somebody.meth()
