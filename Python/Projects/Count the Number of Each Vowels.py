#!/usr/bin/env python3

a = input("Enter a Strings: ")

vowels = "aeious"

a = a.casefold()

count = {}.fromkeys(vowels, 0)

for char in a:
  if char in count:
    count[char]+=1

print(count)
