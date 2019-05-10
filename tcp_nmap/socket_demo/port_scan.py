# -*- coding:utf-8 -*-

import optparse
from socket import *

"""扫描目标主机端口状态"""


def conn_scan(target_host, target_port):
    try:
        conn_socket = socket()
        conn_socket.connect(target_host, target_port)
        print("[+] %s/tcp open" % target_port)
        conn_socket.close()
    except:
        print("[-] %s/tcp closed" % target_port)


def port_scan(target_host, target_ports):
    try:
        target_ip = gethostbyname(target_host)
    except Exception:
        print("[-] Cannot resolve '%s' : Unknown host" % target_host)
    try:
        target_name = gethostbyaddr(target_ip)
        print("[+] Scan resolve for '%s' " % target_name[0])
    except Exception:
        print
        "[+] Scan resolve for '%s' " % target_ip
    setdefaulttimeout(1)
    for target_port in target_ports:
        print("Scanning port " + target_port)
        conn_scan(target_host, target_port)


def main():
    parse = optparse.OptionParser("[*] Usage : %prog -H <target host> -P <target port, target port, ...>")
    parse.add_option("-H", dest="target_host", type="string", help="specify target host")
    parse.add_option("-P", dest="target_port", type="string", help="specify target port")
    (options, args) = parse.parse_args()
    target_host = options.target_host
    target_ports = str(options.target_port).split(",")
    if (target_host is None) | (target_ports is None):
        print(parse.usage)
        exit(0)
    port_scan(target_host, target_ports)


if __name__ == "__main__":
    main()
    # python sock_scan.py -H 192.168.199.1 -P 80,443,23,21,22
