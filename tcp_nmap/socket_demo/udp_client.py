# -* coding:utf-8 --

import socket

target_host = "vip.jd100.com"
target_port = 80

# 建立一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送一些数据
client.sendto("Are You Ok?", (target_host, target_port))

# 接收一些数据
data, addr = client.recvfrom(4096)

print(data, "\n", addr)
