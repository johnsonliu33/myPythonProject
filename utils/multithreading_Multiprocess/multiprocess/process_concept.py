# 每启动一个子进程就从父进程克隆一份数据，进程之间的数据本身是不能共享的。
from multiprocessing import Process
import time, os


def func(title):
    print(title)
    print("modle_name: ", __name__)
    print("parent_name: ", os.getppid())  # 获取父进程ID
    print("process_id: ", os.getpid())  # 获取自己的进程ID


def f(name):
    func("\033[31;1m function f\033[0m")
    print(time.time())
    print("hello", name)


if __name__ == '__main__':
    func('\033[32;1m main process line \033[0m')
    name_list = ("jack", "bob")
    for item in name_list:
        p = Process(target=f, args=(item,))
        p.start()
        p.join()
"""
 main process line
modle_name:  __main__
parent_name:  15876
process_id:  9992
 function f
modle_name:  __mp_main__
parent_name:  9992
process_id:  12044
1557472080.023705
hello jack
 function f
modle_name:  __mp_main__
parent_name:  9992
process_id:  4988
1557472080.232705
hello bob
"""