import socket

if __name__=="__main__":
    socketObj = socket.socket()
    socketObj.connect(("127.0.0.1", 18119))
    print(socketObj.recv(1024).decode("utf-8"))
    for name in [b"Joey", b"Candice"]:
        socketObj.send(name)
        print(socketObj.recv(1024).decode("utf-8"))
    socketObj.send(b"exit")
    socketObj.close()