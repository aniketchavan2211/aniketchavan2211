#!/usr/bin/env python3

text = str(input("Enter a String: "))

def text_to_binary(binary):
  binary = " ".join(format(ord(c), "b") for c in text)
  print (binary)
  return binary

def binary_to_text(normal):
  normal = "".join(chr(int(c,2)) for c in text.split(" "))
  print (normal)
  return normal


person = int(input("Enter number: "))

if person == 1:
  text_to_binary(text)
elif person == 2:
  binary_to_text(text)
else:
  raise print("Enter a valid number")
