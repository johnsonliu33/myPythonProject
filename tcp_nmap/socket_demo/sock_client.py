# -*- coding:utf-8 -*-
import socket

print ("====== socket client ======")
cli = socket.socket()
cli.connect(("127.0.0.1", 2323))
data = cli.recv(1024)
cli.close()
print ("recv: ", data)
