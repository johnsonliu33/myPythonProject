# -*- coding:utf-8 -*-

from optparse import OptionParser
from threading import Thread, Semaphore
from socket import *

screenLock = Semaphore(value=1)  # 当value=1时信号量被锁定，不执行打印操作；当value=0时信号量被释放，执行打印操作


def connScan(target_host, target_port):
    try:
        conn_sock = socket(AF_INET, SOCK_STREAM)
        conn_sock.connect((target_host, target_port))
        conn_sock.send("ViolentPython\r\n")
        results = conn_sock.recv(1024)
        screenLock.acquire()  # 查看信号量
        print
        screenLock.acquire(), "====================="
        print("[+] %d/tcp open " % target_port)
        print("[+] " + str(results))
    except:
        screenLock.acquire()
        print("[-] %d/tcp closed " % target_port)
    finally:
        screenLock.release()  # 重置信号量
        conn_sock.close()


def portScan(target_host, target_ports):
    try:
        target_ip = gethostbyname(target_host)
    except:
        print("[-] Cannot resolve '%s' : Unknown host " % target_host)
        return
    try:
        target_name = gethostbyaddr(target_ip)
        print("[-] Scan resolve for target_name : " + target_name[0])
    except:
        print("[-] Scan resolve for target_ip : " + target_ip)
    setdefaulttimeout(1)
    for port in target_ports:
        test = Thread(target=connScan, args=(target_host, int(port)))
        test.start()


def main():
    usage = "[*] Usage %porg -h <target host> -p <target port>"
    parser = OptionParser(usage)
    parser.add_option("-H", dest="targetHost", type="string", help="specify target host")
    parser.add_option("-P", dest="targetPort", type="string", help="specify target port[s] separated by comma")
    (options, args) = parser.parse_args()
    target_host = options.targetHost
    target_ports = str(options.targetPort).split(", ")
    if (target_host is None) | (target_ports[0] is None):
        print(parser.usage)
        exit(0)

    portScan(target_host, target_ports)


if __name__ == "__main__":
    main()
    # python portScan_thread.py -H 42.62.108.20 -P 22, 80
    # python portScan_thread.py -H vip.jd100.com -P 22
