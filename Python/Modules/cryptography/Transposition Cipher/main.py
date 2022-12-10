#!/usr/bin/env python3

plaintext = input("Enter text: ")

key = 9

ciphertext = [''] * key

for column in range(key):
  pointer = column

  while pointer < len(plaintext):
    ciphertext[column] += plaintext[pointer]

    pointer += key

print("Cipher Text: ", ''.join(ciphertext))
