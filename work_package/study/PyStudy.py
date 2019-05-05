
print ("=================不定长参数函数==================")
def functionname(formal_args, *var_args):
    # * 可以代表一个不定长参数
    print(formal_args)
    print(var_args)
    print(type(var_args))
    print ("----------")
    return True
functionname("这是一个可变参数")
functionname("这是一个可变参数","aaa","bbb","ccc")

print ("================匿名函数的调用===================")


print ("=================类和方法==================")
class Allfc():
    def add(self):
        # 无 return
        print("==add==")
    def acc(self):
        # 有 return
        return "==acc=="
    def aee(self, a, b):
        # 有参数，无默认值
        print (a+b)
    def aff(self, a=1, b=2):
        # 有参数默认值
        print (a+b)
a=Allfc()
a.add()
a.acc()
a.aee(2,3)
a.aff()

print ("================self实例参数===================")
class Count():
    def __init__(self):
        print ("这里是初始化内容")
        self.a = 5
        self.b = 6
    def add(self):
        d = self.a +self.b
        return d
    def acc(self):
        c = self.a - self.b
        return c
    def aee(self):
        e = self.add()*self.acc()
        return e
if __name__ == "__main__":
    #实例化的时候,会先执行初始化__init__的内容
    c = Count()
    print(c.add())
    print(c.acc())
    print(c.aee())

