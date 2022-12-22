#!/usr/bin/env python3
from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

  @abstractstaticmethod
  def person_method():
     """ Interface Methods """

# p1 = IPerson() # instance error
# p1.person_method

class Student(IPerson):

  def __init__(self):
    self.name = "Student"

  def person_method(self):
    print("I am Student")

class Teacher(IPerson):

  def __init__(self):
    self.name = "Teacher"

  def person_method(self):
    print("I am Teacher")

# s1 = Student()
#s1.person_method()

#t1 = Teacher()
#t1.person_method()

class PersonFactory():

  @staticmethod
  def build_person(person_type):
    if person_type == "Student":
      return Student()
    if person_type == "Teacher":
      return Teacher()
    print("Invalid")
    return -1

if __name__ == '__main__':
  choice = input("Type : ")
  person = PersonFactory.build_person(choice)
  try:
    person.person_method()
  except Exception as e:
    pass
