from socket import *
import time
import os
import sys
import pickle

CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K'

def help():
    print("help function")

def download(serverName, serverPort, file_name):
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.bind(('localhost', 5001))
    dataSocket.listen()

    connectionSocket, addr = dataSocket.accept()

    file_name = connectionSocket.recv(1024).decode()
    print("FILE NAME: " + file_name)
    file_size = connectionSocket.recv(1024).decode()

    file = open(file_name, "wb")

    file_bytes = b""

    print("Downloading: " + file_name + " from client")
    done = False
    while not done:
        data = connectionSocket.recv(1024)
        if file_bytes[-3:] == b"EOF":
            done = True
        else:
            file_bytes += data
            print("Bytes recieved: " + str(len(file_bytes)) + " out of " + str(file_size), end="\r") 

    file.write(file_bytes[0:-3])
    file.close()
    dataSocket.close() 
    print("Success: Downloaded " + file_size + " bytes        ")

def upload(serverName, serverPort, file_name):
    time.sleep(1)
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.connect(('localhost', 5001))

    print("Uploading: " + file_name + " to client.")

    file = open(file_name, "rb")
    file_size = os.path.getsize(file_name)

    dataSocket.send(file_name.encode())
    dataSocket.send(str(file_size).encode())

    data = file.read()
    dataSocket.sendall(data)
    dataSocket.send(b"EOF")
    file.close()
    dataSocket.close()
    print("File Upload Successful")

    

def ls(serverName, serverPort):
    time.sleep(1)
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.connect(('localhost', 5001))

    files_list = os.listdir()
    files_list.remove("serv.py")
    files_list.remove("serv_functions.py")
    files_pickle = pickle.dumps(files_list)
    dataSocket.send(files_pickle)
    dataSocket.close()
    print("File List has been sent")

def quit():
    print("quit function")