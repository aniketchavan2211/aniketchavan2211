#!/usr/bin/env python3

num = input("Enter a string:  ")

def float_check(num):

  try:
    float(num)
    print(f"Entered string is a number {num}")
    return True

  except:
    print("Entered string is not number")
    return False

print(float_check(num))
