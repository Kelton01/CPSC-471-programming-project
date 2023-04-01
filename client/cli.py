from socket import *
import os
import sys

#sender = connect, receiver = bind

serverName = sys.argv[1]
serverPort = sys.argv[2]

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

client, addr = clientSocket.accept()

file_name = client.recv(1024).decode()
print(file_name)
sile_size = client.recv(1024).decode()
print(file_size)

file = open(file_name, "wb")

file_bytes = b""

file.write(file_bytes)

file.close()
client.close()