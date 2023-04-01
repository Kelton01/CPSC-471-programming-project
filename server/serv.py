from socket import *
import sys


serverPort = sys.argv[1]

print(serverPort)

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('',serverPort))