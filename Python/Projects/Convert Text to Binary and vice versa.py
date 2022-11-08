#!/usr/bin/env python3

print('\n1) Text to Binary\n')
print('2) Binary to Text\n')

try:
  choice = int(input("Enter: "))
  print('')
  text = str(input("Enter value: "))
  print('')
except Exception as e:
  print('ERROR: ', e)

def text_to_binary(binary):
  binary = " ".join(format(ord(c), "b") for c in text)
  print (int(binary))
  return binary

def binary_to_text(normal):
  normal = "".join(chr(int(c,2)) for c in text.split(" "))
  print (normal)
  return normal

try:
  if choice == 1:
    text_to_binary(text)
  elif choice == 2:
    binary_to_text(text)
  else:
    print('Please enter 0 or 1')
except Exception as e:
  print('ERROR: ',e)
