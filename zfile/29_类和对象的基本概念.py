# class 是一个抽象的集合
# 对象 是一个真是存在的实例

def fun():  # function(函數)
    pass


class ClassName():  # class(类)
    def __init__(self, name, age):  # method(方法)
        self.name = name  # attribute(属性)
        self.age = age  # attribute(属性)
        self._protect_var = "受保护属性"
        self.__private_var = "私有属性"

    def meth(self):  # method(方法)
        print("my name is : {},  age is : {} ".format(self.name, self.age))

    def get_var(self):
        return self.__private_var

    def set_var(self, var):
        self.__private_var = var
        print("class外部可以通过set方法修改ClassName类中的私有属性__protect_var ：{}".format(self.__private_var))

somebody = ClassName(name="python", age=15)
somebody.meth()

print("***class外部可以直接访问ClassName类中的公共属性name***：{}".format(somebody.name))
somebody.name = "***class外部可以直接修改ClassName类中的公共属性name***"
somebody.meth()

print("class外部可以直接访问ClassName类中的受保护属性_protect_var ：{}".format(somebody._protect_var))
somebody._protect_var = "***update公共属性***"
print("class外部可以直接修改ClassName类中的公共属性_protect_var ：{}".format(somebody._protect_var))

# print("class外部 不可以 直接访问ClassName类中的受保护属性_protect_var ：{}".format(somebody.__protect_var))
print("class外部可以通过get方法访问ClassName类中的私有属性__protect_var ：{}".format(somebody.get_var()))
somebody.set_var("***update私有属性***")