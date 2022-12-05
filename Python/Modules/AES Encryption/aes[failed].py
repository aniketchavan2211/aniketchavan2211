#!/usr/bin/env python3

# key must be 16, 24 or 32 bytes long
# text should be 16 bytes

from Crypto.Cipher import AES
key = 'sixteen byte key'
plain = 'text 0f 16 bytes'
Cipher = AES.new(key)
ciphertext = Cipher.encrypt(plain)
print(ciphertext.encode("hex")) # hexadecimal

plaintext = Cipher.decrypt(ciphertext)
print(plaintext)
