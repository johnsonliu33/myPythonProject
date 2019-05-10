import sys
import os


# print(sys.exit("goodbye"))  # 打印"goodbye"
# print(os._exit())  # 不打印直接退出

# sys.exit([args])的参数解析
# 参数为数字的时候，和 shell 退出码意义是一样的，sys.exit(2)和sys.exit(1)只是为了区分结束原因
# 0 ：成功结束
# 1 ：通用错误　　
# 2 ：误用Shell命令
def sys_or_os():
    try:
        sys.exit(0)
    except:
        print("sys===die")
    finally:
        print("sys.exit(0)")

    try:
        os._exit(0)
    except:
        print("os===die")
    print("os._exit(0)")


if __name__ == '__main__':
    sys_or_os()
    """打印：
    sys===die
    sys.exit(0)
    """
