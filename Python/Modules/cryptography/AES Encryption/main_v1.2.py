#!/usr/bin/env python3
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


# without key file, generating key and encrypting text file with generated key

salt = b'\x01z\x04W\xe3\x06\xdd\x90\x9a\xf4@\xdc\x9b\x85\x1exr\xf3\x12\xf8J=\xc0\xfa\x9bN\xa3\xc6>\xd0\t\x9b'
password = "admin"

key = PBKDF2(password, salt, dkLen=32)

# opening encrypted file
with open('encrypted.bin', 'rb') as f:
  iv = f.read(16)
  decrypt_data = f.read()

# decryption
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)
