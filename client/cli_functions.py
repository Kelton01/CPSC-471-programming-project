from socket import *
import os
import sys

def help():
    print("help function")

def get(serverName, serverPort, file_name):
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

    file.write(file_bytes)
    file.close()
    dataSocket.close()

def put(serverName, serverPort, file_name):
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.connect((serverName, serverPort))
    connectionSocket, addr = dataSocket.accept()

    file = open(file_name, "rb")
    file_size = os.path.getsize(file_name)

    datatSocket.send(file_name.encode())
    dataSocket.send(str(file_size).encode())

    data = file.read()
    dataSocket.sendall(data)
    dataSocket.send(b"EOF")
    file.close()
    dataSocket.close()

    

def ls():
    print("list function")

def quit():
    print("quit function")
