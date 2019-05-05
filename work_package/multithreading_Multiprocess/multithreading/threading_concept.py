import threading, time


# 1.创建线程普通方法

def run(n):
    print("task ", n)
    time.sleep(1)
    print("2s")
    time.sleep(1)
    print("1s")
    time.sleep(1)
    print("0s")
    time.sleep(1)


t1 = threading.Thread(target=run, args=("t1",))
t2 = threading.Thread(target=run, args=("t2",))
# t1.start()
# t2.start()
"""
task  t1
task  t2
2s2s

1s1s

0s0s
"""


# 2.继承threading.Thread来自定义线程类，其本质是重构Thread类中的run方法。
class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()  # 重构run函数必须要重写init
        self.n = n

    def run2(self):
        print("task ", self.n)
        time.sleep(1)
        print("2s")
        time.sleep(1)
        print("1s")
        time.sleep(1)
        print("0s")
        time.sleep(1)


if __name__ == "__main__":
    t3 = MyThread("t3")
    t4 = MyThread("t4")
    t3.start()
    t4.start()
