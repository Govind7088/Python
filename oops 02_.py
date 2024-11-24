class Calculator:
  def __init__(self, num):
    self.num=num

  def square(self):
    print(f"The value of {self.num} square is {self.num**2}.")
  
  def squareroot(self):
    print(f"The value of {self.num} squareroot is {self.num**0.5}.")

  def cube(self):
    print(f"The value of {self.num} cube is {self.num**3}.")

a=Calculator(6)
a.square()
a.squareroot()
a.cube()
  