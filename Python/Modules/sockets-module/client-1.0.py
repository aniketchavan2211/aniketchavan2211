#!/usr/bin/env python3
import socket

# Specify server ip
HOST = '127.0.0.1'
PORT = 2211

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello, World!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))
