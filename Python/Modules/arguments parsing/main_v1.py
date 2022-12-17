#!/usr/bin/env python3

def myfunc(*args, **kwargs):
  print(args[0])
  print(args[1])
  print(args[2])
  print(kwargs['KEYWD'])

myfunc('a', 'b', 'c', KEYWD=1)
