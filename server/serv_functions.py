"""
James Pham - jpham25@csu.fullerton.edu
Kelton Benson - kelton01@csu.fullerton.edu
Phuoc Nguyen - phuocnguyen102800@csu.fullerton.edu
Arturo Salazar - arturosi1@csu.fullerton.edu
Kingston Leung - leungkingston@csu.fullerton.edu

CPSC 471-03

"""

from socket import *
import time
import os
import sys
import pickle


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
            print(str(round( len(file_bytes) / int(file_size) * 100,2)) + "% downloaded." , end="\r")

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
    print("List of files has been sent to client.")
