import socket
import threading


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("[*] Received: %s" % request)
    client_socket.send("ACK!")
    client_socket.close()


bind_ip = "127.0.0.1"
bind_port = 3344
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
conn, addr = server.accept()
print("[*] Listenting on %s:%d" % (bind_ip, bind_port))
print("[*] %s   %s  " % (conn, addr))
while True:
    client, addr = server.accept()
    print("[*] Accepted connection from: %s%d" % (addr[0], addr[1]))
    client_handler = threading.Thread(target=handle_client, args=(client))
    client_handler.start()
