# sys.argv 返回一个序列
import sys

print(sys.argv[0])  # 第一个参数是当前文件本身="D:/myPythonProject/work_package/study/sys_argv.py"


def func():
    usage = """usage: sys_argv.py <args1> <args2>\n     eg : sys_argv.py args1 args2"""
    if len(sys.argv) < 3:
        print(usage)
    else:
        print(sys.argv[1])
        print(sys.argv[2])


if __name__ == '__main__':
    func()
