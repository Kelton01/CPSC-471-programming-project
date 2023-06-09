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

def help():
    print("unknown command.")

def download(serverName, serverPort, file_name):
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.bind(('localhost', 5001))
    dataSocket.listen()

    connectionSocket, addr = dataSocket.accept()

    file_name = connectionSocket.recv(1024).decode()
    file_size = connectionSocket.recv(1024).decode()

    file = open(file_name, "wb")

    file_bytes = b""

    print("Downloading: " + file_name + " from server.")
    done = False
    while not done:
        data = connectionSocket.recv(1024)
        if file_bytes[-3:] == b"EOF":
            done = True
        else:
            file_bytes += data
            print(str((round( len(file_bytes) / int(file_size),2) * 100)) + "% downloaded." , end="\r")

    file.write(file_bytes[0:-3])
    file.close()
    dataSocket.close()
    print("Success: Downloaded: " + file_name + "        ")

def upload(serverName, serverPort, file_name):
    time.sleep(1)
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.connect(('localhost', 5001))


    file = open(file_name, "rb")
    file_size = os.path.getsize(file_name)

    print("Uploading: " + file_name + " to server.")

    dataSocket.send(file_name.encode())
    dataSocket.send(str(file_size).encode())

    data = file.read()
    dataSocket.sendall(data)
    dataSocket.send(b"EOF")
    file.close()
    dataSocket.close()
    print("File Upload Successful")

    

def ls(serverName, serverPort):
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.bind(('localhost', 5001))
    dataSocket.listen()
    connectionSocket, addr = dataSocket.accept()

    data = connectionSocket.recv(1024)
    file_names = pickle.loads(data)
    print('~~~~~~Files in Directory~~~~~~ \n')
    for x in file_names:
        print(f'• {x}\t')
    dataSocket.close()

