#!/usr/bin/env python3

string = input('Enter anything: ')

try:
  num = int(input('Enter number: '))
  print(string + num)
except Exception as e:
  print(' Error: ', e)
