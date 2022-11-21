#!/usr/bin/env python3

# Hashing Data
import hashlib


m = hashlib.md5() # specifying variable m, module_name.HashTypeFunction()
m.update(b"A") # hash 'A'
print(m.digest())  # binary
print(m.hexdigest()) # hexidecimal
