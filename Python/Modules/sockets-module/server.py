#!/usr/bin/env python3
import socket

soc = socket.socket(socket.AF_IRDA, socket.SOCK_STREAM)

soc.bind((socket.gethostname(), 2211))

soc.listen(5)

while True:
  client, address = soc.accept()
  print(f"Connection established with {client}")
  client.send(bytes("Hey, This is message from server to client.", "utf-8"))
