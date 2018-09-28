import socket
import threading
import time

def handleClient(socketObj, address):
    print("Receive from %s:%s" % address)
    socketObj.send(b"welcome")
    while True:
        data = socketObj.recv(1024)
        time.sleep(1)
        if not data or data.decode("utf-8")=="exit":
            break
        socketObj.send(("Hello %s" % data.decode("utf-8")).encode("utf-8"))
    socketObj.close()
    pass

if __name__ == "__main__":
    socketObj = socket.socket()
    socketObj.bind(("127.0.0.1", 18119))
    socketObj.listen(5)
    print("Waiting for connection...")
    while True:
        newSockectObj, address = socketObj.accept()
        newThread = threading.Thread(target=handleClient, args=(newSockectObj, address))
        newThread.start()