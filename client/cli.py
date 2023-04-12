from socket import *
from cli_functions import *
import os
import sys
import pickle

# sender = connect, receiver = bind
# we need to use pickle to take the list of strings from terminal input to safely send to server

"""
This initial connection is the CONTROL connection, which lasts throughout the session and is used to
transfer all commands
"""
serverName = sys.argv[1]
serverPort = sys.argv[2]

controlSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
controlSocket.connect((serverName, serverPort))
connectionSocket, addr = controlSocket.accept()

"""
Each time a new command is inputted into the terminal, we split up the entire command into a list of strings
This new list of strings is also send to the server using the CONTROL connection, so the server can also prepare
to either send or receive data depending on which command is used.
"""
Disconnect = False
while not Disconnect:
    print("ftp> ", end = '')
    cmd = input("")
    all_words = cmd.split()
    controlCommand = pickle.dumps(all_words)
    if all_words[0] == "get" and len(all_words) == 2:
        controlSocket.send(controlCommand)
        get(serverName, serverPort, all_words[1])

    elif all_words[0] == "put" and len(all_words) == 2:
        controlSocket.send(controlCommand)
        put(serverName, serverPort, all_words[1])

    elif all_words[0] == "ls" and len(all_words) == 1:
        controlSocket.send(controlCommand)
        ls(serverName, serverPort)

    elif all_words[0] == "quit" and len(all_words) == 1:
        controlSocket.send(controlCommand)
        controlSocket.close()
        Disconnect = True
    else:
        help()


