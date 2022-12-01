#!/usr/bin/env python3
import socket
import threading

import rsa

public_key, private_key = rsa.newkeys(1024)
public_partner = None

choice = input ("Do you want to host (1) or to connect (2): ")

if choice == "1":
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(("127.0.0.1", 8080))
  server.listen()

  client, _ = server.accept()
  client.send(public_key.save_pkcs1("PEM"))
  public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))

elif choice == "2":
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect(("127.0.0.1", 8080))
  public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
  client.send(public_key.save_pkcs1("PEM"))

else:
  exit()

def sending_message(c):
  while True:
    message = input("")
    c.send(rsa.encrypt(message.encode(), public_partner))
    # c.send(message.encode()) # Unencrypted

    print("You: " + message)

def receiving_message(c):
  while True:
    print("Partner: " + rsa.decrypt(c.recv(1024), private_key).decode())
    # print("Partner: " + c.recv(1024).decode()) # Unencrypted

threading.Thread(target=sending_message, args=(client, )).start()
threading.Thread(target=receiving_message, args=(client, )).start()

