#!/usr/bin/env python3

# seq 1 to 9,000,000

def mygenerator(n):
  for x in range(n):
    yield x ** 3 # cube of x

values = mygenerator(100)

# print(next(values))
# print(next(values))
# print((values))

## prints all values
# for x in values:
#   print(x)

def infinite_sequence():
  result = 1
  while True:
    yield result
    result *= 5

values = infinite_sequence()

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
