"""
James Pham - jpham25@csu.fullerton.edu
Kelton Benson - kelton01@csu.fullerton.edu
Phuoc Nguyen - phuocnguyen102800@csu.fullerton.edu
Arturo Salazar - arturosi1@csu.fullerton.edu
Kingston Leung - leungkingston@csu.fullerton.edu

CPSC 471-03

"""

from socket import *
from serv_functions import *
import os
import sys
import pickle

#sender = connect, receiver = bind

serverPort = int(sys.argv[1])

if len(sys.argv) != 2:
    print("Please specify the <port>")
    exit()

#controlSocket = socket(AF_INET, SOCK_STREAM)

#controlSocket.bind(('',serverPort))

#controlSocket.listen(1)
#print("The server is ready to receive")
while 1:
    Disconnect = False
    controlSocket = socket(AF_INET, SOCK_STREAM)

    controlSocket.bind(('',serverPort))

    controlSocket.listen(1)
    print("The server is ready to receive new client connection")
    connectionSocket, addr = controlSocket.accept()
    print("client connection established")
    while Disconnect == False:
        data = connectionSocket.recv(1024)
        all_words = pickle.loads(data)
        if all_words[0] == "get":
            if os.path.isfile(all_words[1]):
                connectionSocket.send('y'.encode())
                upload(addr[0], addr[1], all_words[1])
            else:
                connectionSocket.send('n'.encode())

        elif all_words[0] == "put" and len(all_words) == 2:
            download(addr[0], addr[1], all_words[1])

        elif all_words[0] == "ls" and len(all_words) == 1:
            ls(addr[0], addr[1])

        elif all_words[0] == "quit" and len(all_words) == 1:
            controlSocket.close()
            print("Previous client connection has been closed")
            Disconnect = True
