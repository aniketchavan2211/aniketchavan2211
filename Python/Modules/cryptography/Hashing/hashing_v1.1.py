#!/usr/bin/env python3
import hashlib

path = r"text.txt"

with open(path, 'rb') as file:
  context = file.read()
  md5 = hashlib.md5()
  sha1 = hashlib.sha1()
  sha224 = hashlib.sha224()
  sha256 = hashlib.sha256()
  sha384 = hashlib.sha384()
  sha512 = hashlib.sha512()
  sha3_224 = hashlib.sha3_224()
  sha3_256 = hashlib.sha3_256()
  sha3_384 = hashlib.sha3_384()
  sha3_512 = hashlib.sha3_512()
  shake_128 = hashlib.shake_128()
  shake_256 = hashlib.shake_256()
  blake2b = hashlib.blake2b()
  blake2s = hashlib.blake2s()

  md5.update(context)
  sha1.update(context)
  sha224.update(context)
  sha256.update(context)
  sha384.update(context)
  sha512.update(context)
  sha3_224.update(context)
  sha3_256.update(context)
  sha3_384.update(context)
  sha3_512.update(context)
  shake_128.update(context)
  shake_256.update(context)
  blake2b.update(context)
  blake2s.update(context)

  print(f'Text: {context}\n')
  print('Hash Value:\n')
  print('{} : {}'.format(md5.name, md5.hexdigest()))
  print('{} : {}'.format(sha1.name, sha1.hexdigest()))
  print('{} : {}'.format(sha224.name, sha224.hexdigest()))
  print('{} : {}'.format(sha256.name, sha256.hexdigest()))
  print('{} : {}'.format(sha384.name, sha384.hexdigest()))
  print('{} : {}'.format(sha512.name, sha512.hexdigest()))
  print('{} : {}'.format(sha3_224.name, sha3_224.hexdigest()))
  print('{} : {}'.format(sha3_256.name, sha3_256.hexdigest()))
  print('{} : {}'.format(sha3_384.name, sha3_384.hexdigest()))
  print('{} : {}'.format(sha3_512.name, sha3_512.hexdigest()))
  print('{} : {}'.format(shake_128.name, shake_128.hexdigest(1)))
  print('{} : {}'.format(shake_256.name, shake_256.hexdigest(1)))
  print('{} : {}'.format(blake2b.name, blake2b.hexdigest()))
  print('{} : {}'.format(blake2s.name, blake2s.hexdigest()))
