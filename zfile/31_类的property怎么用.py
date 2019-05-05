class People:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        # 格式的规范
        return self.__name.upper()

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        # 做一些合法的检查
        self.__age = age


someone = People(name="jack", age=18)
print(someone.name)  # JACK
print(someone.age)  # 18
someone.name = "black"
someone.age = 30
print(someone.name)  # BLACK
print(someone.age)  # 30
