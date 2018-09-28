import socket
import time
import threading

HOST_IP = "127.0.0.1"
PORT = 18119
SLEEP_TIME = 1
RECV_BUFF_MAX = 1024
EXIT_CODE = b"exit"
CODING = "utf-8"
MAX_CLIENT = 5
ACC_CODE = b"Welcome"

def handleClient(clientSocket, clientAddress):
    print("Receive message from %s:%s" % clientAddress)
    clientSocket.send(ACC_CODE)
    while True:
        data = clientSocket.recv(RECV_BUFF_MAX)
        time.sleep(SLEEP_TIME)
        if not data or data==EXIT_CODE:
            break
        sendMsg = "Hello %s" % data.decode(CODING)
        clientSocket.send(sendMsg.encode(CODING))
    clientSocket.close()

print("Start!")
listenSocket = socket.socket()
listenSocket.bind((HOST_IP, PORT))
listenSocket.listen(MAX_CLIENT)
while True:
    acceptClient, address = listenSocket.accept()
    workingThread = threading.Thread(target=handleClient, args=(acceptClient, address))
    workingThread.start()
