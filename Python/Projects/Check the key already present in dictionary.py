#!/usr/bin/env python3

dict1 = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

key = input('Enter a key: ')

if key in dict1.keys():
  print('key is present')
else:
  print('key not FOUND')
