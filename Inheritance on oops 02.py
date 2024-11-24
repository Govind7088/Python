''' Create a class pets from a class animals and further create class dog from pets. 
Add a method bark to class dog. '''

class Animals():
  animlaType="Horse"

class Pets:
  petType="Black"

class Dog:
  @staticmethod
  def bark():
    print("Bow Bow!")

d=Dog()
d.bark()