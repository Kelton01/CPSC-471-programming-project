from socket import *
from cli_functions import *
import os
import sys

#sender = connect, receiver = bind

#serverName = sys.argv[1]
#serverPort = sys.argv[2]

#clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#clientSocket.connect((serverName, serverPort))
#connectionSocket, addr = clientSocket.accept()

Disconnect = False

while not Disconnect:
    print("ftp> ", end = '')
    cmd = input("")
    all_words = cmd.split()
    if all_words[0] == "get" and len(all_words) == 2:
        get(serverName, serverPort, all_words[1])
    elif all_words[0] == "put" and len(all_words) == 2:
        put(serverName, serverPort, all_words[1])
    elif all_words[0] == "ls" and len(all_words) == 1:
        ls(serverName, serverPort)
    elif all_words[0] == "quit" and len(all_words) == 1:
        connectionSocket.close()
        Disconnect = True
    else:
        help()


"""
client, addr = clientSocket.accept()

file_name = client.recv(1024).decode()
print(file_name)
sile_size = client.recv(1024).decode()
print(file_size)

file = open(file_name, "wb")

file_bytes = b""

file.write(file_bytes)

file.close()
"""


