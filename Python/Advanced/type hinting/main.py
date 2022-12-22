#!/usr/bin/env python3

# expect parameter p1 as integer
def myfunc(p1: int) -> str:
  print (p1)
  return f"{p1 + 10}"

# myfunc("Hello")

# if string is pass no matter it will also print
# Hello

# mypy main.py
# print (myfunc("Hello")) # throw an error msg
print (myfunc(10)) # success

def other(p2: str):
  print(p2)

other(myfunc(20))
# mypy main.py
# 30

# expecting list of integers
def otherfunc(p3: list[int]):
  pass
