from socket import *
from serv_functions import *
import os
import sys

#sender = connect, receiver = bind

serverPort = sys.argv[1]

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(('',serverPort))

print("The Server is ready to receive")

file = open("image.png", "rb")
file_size = os.path.getsize("image.png")

serverSocket.send("received_image.png".encode())
serverSocket.send(str(file_size).encode())

data = file.read()
serverSocket.sendall(data)
serverSocket.send(b"<END>")

file.close()
serverSocket.close()