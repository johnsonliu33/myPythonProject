import pickle


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("My name is {}, I'm {}".format(self.name, self.age))


# pc = People("Jack", 33)
# f = open("pickle_demo", "wb")
# pickle.dump(pc, f)  # pickle.dump以二进制形式写入
# f.close()

f = open("pickle_demo", "rb")
pic = pickle.load(f)  # pickle写入只能用pickle读取，其他编程语言不能读取,读取恶意代码有风险
f.close()
# pickle读取的时候必须要有写入的方法
print(pic, pic.name, pic.age)
pic.hello()  # 可以调用People类中的hello方法
