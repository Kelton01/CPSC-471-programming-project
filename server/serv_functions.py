
from socket import *
import os
import sys

def help():
    print("help function")

def download(serverName, serverPort, file_name):
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.connect((serverName, serverPort))
    dataSocket.listen()

    connectionSocket, addr = dataSocket.accept()

    file_name = connectionSocket.recv(1024).decode()
    file_size = client.recv(1024).decode()

    file = open(file_name, "wd")

    file_bytes = b""

    done = False
    while not done:
        data = client.recv(1024)
        if file_bytes[-3:] == b"EOF":
            done = True
        else:
            file_bytes += data

    file.write(file_bytes[0:-3])
    file.close()
    dataSocket.close()

def upload(serverName, serverPort, file_name):
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.connect((serverName, serverPort))
    connectionSocket, addr = dataSocket.accept()

    file = open(file_name, "rb")
    file_size = os.path.getsize(file_name)

    dataSocket.send(file_name.encode())
    dataSocket.send(str(file_size).encode())

    data = file.read()
    dataSocket.sendall(data)
    dataSocket.send(b"EOF")
    file.close()
    dataSocket.close()

    

def ls():
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.connect((serverName, serverPort))
    connectionSocket, addr = dataSocket.accept()

    files_list = os.listdir()
    files_list.remove("serv.py")
    files_list.remove("serv_functions.py")
    files_pickle = pickle.dumps(files)
    dataSocket.send(files_pickle)
    dataSocket.close()
    print("File List has been sent")

def quit():
    print("quit function")