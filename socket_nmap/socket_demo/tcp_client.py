# -* coding:utf-8 --

import socket

target_host = "vip.jd100.com"
target_port = 80

# 建立一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接客户端
client.connect((target_host, target_port))

# 发送一些数据
client.send("GET / HTTP/1.1\r\nHost:jd100.com\r\n\r\n")

# 接受一些数据
response = client.recv(4096)

print("recv:\n\n", response)
