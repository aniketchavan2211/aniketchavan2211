#!/usr/bin/env python3

a = input('Enter String: ')

w = a.split()

for i in range(len(w)):
  w[i] = w[i].lower()

w.sort()

for i in w:
  print(w)
