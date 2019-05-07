class Student:
    count = 0

    def __init__(self, name):
        self.name = name


print(Student.count)  # 0
s1 = Student(name="jack")
print(s1.name)  # jack
print(s1.count)  # 0
s1.name = "black"
s1.count = 6
print(Student.count)  # 0 修改实例属性不会修改类属性
print(s1.name)  # black
print(s1.count)  # 0
s2 = Student("white")
print(s2.count)  # 0 修改s1的实例属性不会改变s2的实例属性


class Teacher:
    num = 0

    def __init__(self, user):
        Teacher.num += 1
        self.user = user


t1 = Teacher("zhangsan")
t2 = Teacher("lisi")
t3 = Teacher("wangwu")
print(Teacher.num)  # 3  每次实例化时，类属性num都会+1
