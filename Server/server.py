from temps import temps
from temps import random_string
import socket
import time

host = "localhost"
port = 6996 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#creates socket with socket object s;
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(2)

clientsocket, address = s.accept()
print(f"Connection from {address} has been done")
##clientsocket.send(bytes("Welcome to server\n","utf-8"))

while True:
    msg = temps()
    clientsocket.send(bytes(msg,"utf-8"))
    time.sleep(1)

