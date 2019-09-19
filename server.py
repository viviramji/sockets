import socket
import select #
import pickle

#pickle serialize data

HEADERSIZE = 10


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    d = {1:"this", 2:" is ", 3:" a dictionary"}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", "utf-8") + msg
    
    clientsocket.send(msg)
