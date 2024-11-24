'''
def greet(name):
  a=("Hello, Good Morning, " + name)
  return a
n=input("Enter Your Name\n ")
print(greet(n))

'''
'''
def sum(num1,num2):
  a=num1+num2
  return a
num1=int(input("Enter the first number\n"))
num2=int(input("Enter the first number\n"))
print(sum(num1,num2))

'''

def percentage(marks):
  p=(sum(marks)/500)*100
  return p
marks1=[50, 34, 54, 70, 60]
marks2=[90, 45, 76, 78, 56]
marks3=[64, 54, 78, 89, 98]
marks4=[76, 75, 89, 76, 70]
marks5=[92, 90, 95, 76, 65]
print(percentage(marks1))
print(percentage(marks2))
print(percentage(marks3))
print(percentage(marks4))
print(percentage(marks5))

