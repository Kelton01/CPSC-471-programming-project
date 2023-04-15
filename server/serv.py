from socket import *
from serv_functions import *
import os
import sys

#sender = connect, receiver = bind

# (note) need to cast the string argument -> int
serverPort = int(sys.argv[1])

# (note) line below changes to the file directory to the files folder to receive the files
# os.chdir("../files")
# print(current

# (note) since we imported * no need to socket.socket
serverSocket = socket(AF_INET, SOCK_STREAM)

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