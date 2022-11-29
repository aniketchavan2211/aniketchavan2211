#!/usr/bin/env python3
import socket

# host = socket.gethostname(socket.gethostname())
# return the IP Address of host machine
# For example taken localhost(127.0.0.1) IP Addr
HOST = '127.0.0.1' # <ip address>

# Dont't take well-known ports or Reserved ports
PORT = 2211 # 5901, 8000, 8080,etc

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5) # limit connection: 5


while True:
  communication_socket, address = server.accept()
  print(f"Connected to {address}")
  message = communication_socket.recv(1024).decode('utf-8')
  print(f"Message from Client is:\033[1;31m {message}\033[0m")
  communication_socket.send(f"Got your message! Thank you!".encode('utf-8'))
  communication_socket.close()
  print(f"Connection with {address} ended!")

