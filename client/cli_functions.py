from socket import *
import os
import sys

def help():
    print("help function")

def get(serverName, serverPort, file_name):
    print("get function")

def put(serverName, serverPort, file_name):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    connectionSocket, addr = clientSocket.accept()

    file = open(file_name, "rb")
    file_size = os.path.getsize(file_name)

    clientSocket.send(file_name.encode())
    clientSocket.send(str(file_size).encode())

    data = file.read()
    clientSocket.sendall(data)
    clientSocket.send(b"UPLOAD FINISHED")
    clientSocket.close()

    

def ls():
    print("list function")

def quit():
    print("quit function")