import socket
import os


def check_port(host, port):
    """检查指定端口是否被占用"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        sock.shutdown(2)
    except OSError as msg:
        print("port %s is availible!" % port)
        print(msg)
        return True
    else:
        print("port %s is use!" % port)
        return False


def release_port(port):
    """释放指定的端口"""
    # 查找对应的端口
    cmf_find = "netstat -ano | findstr %s" % port
    print(cmf_find)

    # 返回执行后的结果
    result = os.popen(cmf_find).read()
    print(result)
    # 获取端口对应的pid
    if str(port) and "LISTENING" in result:
        str_list = result.split()
        pid = str_list[4]
        # 关闭被占用端口的pid
        cmd_kill = "taskkill -f -pid %s" % pid
        print(cmd_kill)
        os.popen(cmd_kill)
    else:
        print("port %s is available!" % port)


# Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
# 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
# Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
if __name__ == '__main__':
    host = "127.0.0.1"
    port = 4723
    # check_port(host, port)
    release_port(port)
