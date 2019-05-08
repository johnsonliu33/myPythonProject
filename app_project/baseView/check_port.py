import socket


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


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 4723
    res = check_port(host, port)
    print(res)
