#!/usr/bin/env python3

class Person:

  def __init__(self, name, age, gender):

    self.__name = name
    self.__age = age
    self.__gender = gender


# this will not work because class is set to private __name, __age, __gender.
# p1 = Person(...hdo)
# p1.__name = "anc"

# setters & getters

  @property
  def Name(self):
    return self.__name

  @Name.setter
  def Name(self, value):
    if value == "alexa":
      self.__name = "Default Name"
    else:
      self.__name = value

#p1 = Person("Mike", 20, "male")
#print(p1.Name) # Mike

#p1.Name = "alexa"
#print(p1.Name) # Mike Default Name

# static methods

  @staticmethod
  def mymethod():
    print("Hello, World")

Person.mymethod()
