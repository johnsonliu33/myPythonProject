import argparse


def get_args():
    descrip = """
        this is a calculator:
    https://yq.aliyun.com/articles/626646?utm_content=m_1000013890
    """
    parser = argparse.ArgumentParser(description=descrip)
    # 设置 -v 为输出程序版本号;  %(prog)s 代表自己的脚本的名称
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")
    # 添加一个必填参数sourceDir;  help是帮助信息;  默认参数类型是str,指定参数类型type=Object.
    parser.add_argument("sourceDir", help="select source directory")
    # 添加一个不带"-"前缀的选填参数; nargs="?"表示选填,"?"表示可以接受0个或1个值.
    parser.add_argument("targetDir", help="select target directory", nargs="?")
    # 添加一个带"-"前缀的选填参数; 加上"-"表示选填参数
    parser.add_argument("-a", "--add", help="add something")
    # 添加一个互相排斥的二选一的选填参数
    group = parser.add_mutually_exclusive_group()
    # action="store_true"表示这个参数不需要填写值，直接写参数就可以了;输出为布尔值.
    group.add_argument("-m", "--move", help="The way to operate the file is to move", action="store_true")
    group.add_argument("-c", "--copy", help="The way to operate the file is to copy", action="store_true")
    args = parser.parse_args()

    # 打印usage
    parser.print_usage()
    """usage: argParse.py [-h] [-v] [-a ADD] [-m | -c] sourceDir [targetDir]
    """
    # 打印help信息
    parser.print_help()
    """usage: argParse.py [-h] [-v] [-a ADD] [-m | -c] sourceDir [targetDir]

    this is a calculator:
    https://yq.aliyun.com/articles/626646?utm_content=m_1000013890

    positional arguments:
        sourceDir          select source directory
        targetDir          select target directory

    optional arguments:
        -h, --help         show this help message and exit
        -v, --version      show program's version number and exit
        -a ADD, --add ADD  add something
        -m, --move         The way to operate the file is to move
        -c, --copy         The way to operate the file is to copy
    """
    # 输出 usage
    parser.format_usage()  # 不打印
    # 输出 help
    parser.format_help()  # 不打印
    # 输出后打印
    print("format_help:  ", parser.format_help())
    """format_help:   usage: argParse.py [-h] [-v] [-a ADD] [-m | -c] sourceDir [targetDir]

    this is a calculator:
    https://yq.aliyun.com/articles/626646?utm_content=m_1000013890

    positional arguments:
        sourceDir          select source directory
        targetDir          select target directory

    optional arguments:
        -h, --help         show this help message and exit
        -v, --version      show program's version number and exit
        -a ADD, --add ADD  add something
        -m, --move         The way to operate the file is to move
        -c, --copy         The way to operate the file is to copy
    """


if __name__ == '__main__':
    get_args()
