#!/usr/bin/env python3
import socket

soc = socket.socket(socket.AF_IRDA, socket.SOCK_STREAM)

soc.connect((socket.gethostname(),2211))

while True:
  msg = soc.recv(1024)
  print(msg.decode('utf-8'))
