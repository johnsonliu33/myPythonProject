import threading, time


# 1.创建线程普通方法

def run1(n):
    print("task ", n)
    time.sleep(1)
    print("2s")
    time.sleep(1)
    print("1s")
    time.sleep(1)
    print("0s")
    time.sleep(1)


t1 = threading.Thread(target=run1, args=("t1",))
t2 = threading.Thread(target=run1, args=("t2",))
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

    def run(self):  # run方法名称不能变
        print("MyThread ", self.n)
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
    # t3.start()
    # t4.start()
"""
MyThread  t3
MyThread  t4
2s2s

1s1s

0s0s
"""


# 3.计算子线程执行的时间
# 注：sleep的时候是不会占用CPU的，在sleep的时候操作系统会把线程暂时挂起。
# join() 等此线程执行完后，再执行其他线程或主线程
# threading.current_thread() 输出当前线程

def run3(k):
    print("\ntask ", k, threading.current_thread())
    time.sleep(1)
    print("3s")
    time.sleep(1)
    print("2s")
    time.sleep(1)
    print("1s")


strat_time = time.time()
t_obj = []
for i in range(3):
    t = threading.Thread(target=run3, args=("t-%s" % i,))
    # t.start()
    # t_obj.append(t)
"""
task  t-0 <Thread(Thread-5, started 8828)>

task  t-1 <Thread(Thread-6, started 8372)>

task  t-2 <Thread(Thread-7, started 9524)>
3s3s

3s
2s2s

2s
1s1s

1s
"""
for tmp in t_obj:
    t.join()  # 为每个子线程添加join之后，主线程就会等这些子线程执行完之后再执行
print("cost: ", time.time() - strat_time)  # 主线程    cost:  3.002000093460083
print(threading.current_thread())  # 输出当前线程    <_MainThread(MainThread, started 8832)>


# 4统计当前活跃的线程数
# 由于主线程比子线程快很多，当主线程执行active_count()时，其他子线程都还没执行完成，
# 因此利用主线程统计活跃的线程数num=sub_num(子线程数)+1(主线程本身)

def run4(x):
    print("task ", x)
    time.sleep(1)  # 子线程暂停1s


for j in range(3):
    t4 = threading.Thread(target=run4, args=("t-%s" % j,))
    t4.start()
time.sleep(0.5)  # 主线程暂停0.5s
print(threading.active_count())  # 输出当前你活跃的线程数4


# 由于主线程比子线程快很多，当主线程执行active_count()时，其他子线程都还没执行完成，
# 因此利用主线程统计活跃的线程数num=1(主线程本身)
def run5(x):
    print("task ", x)
    time.sleep(0.5)  # 子线程暂停0.5s


for j in range(3):
    t4 = threading.Thread(target=run5, args=("t-%s" % j,))
    t4.start()
time.sleep(1)  # 主线程暂停1s
print(threading.active_count())  # 输出当前你活跃的线程数1

# 在Python内部默认会等待最后一个进程执行完后执行exit()，或者说在python内部有一个隐藏的join()
