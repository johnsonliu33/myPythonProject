# 每启动一个子进程就从父进程克隆一份数据，进程之间的数据本身是不能共享的。
from multiprocessing import Process
import time
def f(name):
    time.sleep(2)
    print("hello ",name)
if __name__ == '__main__':
    p=Process(target=f,args=("bob",))
    p.start()
    p.join()




