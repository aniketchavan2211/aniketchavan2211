#!/usr/bin/env python3

class Vector():

  def __init__(self, x ,y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

  def __repr__(self):
    return f"X: {self.x}, Y: {self.y}"

  def __len(self):
    return 10

  def __call_(self):
    print("Hello, This is a called")

v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2
# v3 = v1 + v2 is not working so used magic methods

print(v3.x)
# 60
print(v3.y)
# 80

print(v3)

# print(len(v3)) # 10
