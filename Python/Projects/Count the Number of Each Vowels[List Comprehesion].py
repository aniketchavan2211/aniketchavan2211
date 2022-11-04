#!/usr/bin/env python3

a = input("Enter a strings: ")

vowels = 'aeiou'

a = a.casefold()

count = {key:sum([1 for char in a if char == key]) for key in vowels}

print(count)
