import socket
import time
#Header is for give some information, e.g. how long is ur msg

HEADERSIZE = 10


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    msg = "Hello from the server"
    msg = f"{len(msg):<{HEADERSIZE}}" + msg
    
    clientsocket.send(bytes(msg, 'utf-8'))
    
    while True:
        time.sleep(3)
        msg = f"The time is: {time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}" + msg
        clientsocket.send(bytes(msg, 'utf-8'))
