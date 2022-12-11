#!/usr/bin/env python3

#def mydecorator(function):
#
#  def wrapper(*args, **kwargs):
#    print("I am decorating your func!")
#    function(*args, **kwargs)
#  return wrapper
#
#"""
#def hello():
#  print("Hello")
#"""
#
#@mydecorator      # mydecorator(hello)()
#def hello(person):
#  print(f"Hello {person}")
#
#
#hello('Alex')

## Return
def mydecorator(function):

  def wrapper(*args, **kwargs):
    print("I am decorating your func!")
    return function(*args, **kwargs)
  return wrapper

"""
def hello():
  print("Hello")
"""

@mydecorator      # mydecorator(hello)()
def hello(person):
  return f"Hello {person}!"


print(hello('Alex'))
