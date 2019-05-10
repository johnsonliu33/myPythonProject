# -*- coding:utf-8 -*-
import socket

print ("====== socket server ======")
sc = socket.socket()
sc.bind(("127.0.0.1", 2323))
sc.listen(5)
while 1:
    conn, address = sc.accept()
    print ("a new connect :", address)
    conn.sendall("Hello world")
    conn.close()
