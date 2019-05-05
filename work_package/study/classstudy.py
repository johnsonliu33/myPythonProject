class Student:
    classroom = '101'
    address = 'beijing' 

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        print('%s: %s' % (self.name, self.age))

if __name__ == "__main__":
    li = Student("李四", 24)
    zhang = Student("张三", 23)
    print(li.name)
    print(li.age)
    print(zhang.name)
    print(zhang.age)
