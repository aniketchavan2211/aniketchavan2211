#!/usr/bin/env python3
import hashlib

# print(hashlib.sha256("Hello World".encode()).hexidigest())

NONCE_LIMIT = 100000000000

zeroes = 8

def mine(block_number, transactions, previous_hash):
  for nonce in range (NONCE_LIMIT):
    base_text = str(block_number) + transactions + previous_hash + str(nonce)
    hash_try = hashlib.sha256(base_text.encode()).hexdigest()
    if hash_try.startswith('0' * zeroes):
      print(f"Found Hash with Nonce: {nonce}")
      return hash_try
  return -1

block_number = 24
transactions = "5tr65r6dfw3yedf3"
previous_hash = "trf7tfdi724gfi74r7fdzfd"

# combined_text = str(block_number) + transactions + previous_hash + str(107617)
# print(hashlib.sha256(combined_text.encode()).hexdigest())

mine(block_number, transactions, previous_hash)
