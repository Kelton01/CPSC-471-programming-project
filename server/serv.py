from socket import *
from serv_functions import *
import os
import sys
import pickle

#sender = connect, receiver = bind

serverPort = sys.argv[1]

if len(sys.argv) != 2:
    print("Please specify the <port>")
    exit()

controlSocket = socket(AF_INET, SOCK_STREAM)

controlSocket.bind(('',serverPort))

controlSocket.listen(1)
print("The server is ready to receive")

while 1:
    connectionSocket, addr = controlSocket.accept()
    Disconnect = False
    while not Disconnect:
        data = connectionSocket.recv(1024)
        all_words = pickle.loads(data)
        if all_words[0] == "get":
            print('1')
            controlSocket.send(controlCommand)
            upload(addr, connectionSocket, all_words[1])

        elif all_words[0] == "put" and len(all_words) == 2:
            print('2')
            controlSocket.send(controlCommand)
            download(addr, connectionSocket, all_words[1])

        elif all_words[0] == "ls" and len(all_words) == 1:
            print('3')
            controlSocket.send(controlCommand)
            ls(addr, connectionSocket)

        elif all_words[0] == "quit" and len(all_words) == 1:
            print('4')
            controlSocket.send(controlCommand)
            controlSocket.close()
            Disconnect = True
        else:
            help()
