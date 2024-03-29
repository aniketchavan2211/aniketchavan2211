#!/usr/bin/env python3
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 8000))

done = False

while not done:
  client.send(input("Message: ").encode('utf-8'))
  msg = client.recv(1024).decode('utf-8')
  if msg == 'quit':
    done = True
  else:
    print(msg)

client.close()
