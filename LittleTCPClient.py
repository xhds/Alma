import socket

HOST_IP = "127.0.0.1"
PORT = 18119
RECV_BUFF_MAX = 1024
EXIT_CODE = b"exit"
CODING = "utf-8"

workingSocket = socket.socket()
workingSocket.connect((HOST_IP, PORT))
print(workingSocket.recv(RECV_BUFF_MAX).decode(CODING))
for name in [b"Fuck", b"YOU"]:
    workingSocket.send(name)
    print(workingSocket.recv(RECV_BUFF_MAX).decode(CODING))
workingSocket.send(EXIT_CODE)
workingSocket.close()