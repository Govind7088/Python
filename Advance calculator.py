def factorial(a):
  c=1
  for i in range(c,a+1):
    c=c*i
  print(c)
def squareroot(a):
   result=a**0.5
   print(result)
def advance_calculator():
  print("Enter the Number")
  value_one = int(input("Enter the first Number : "))
  value_two = int(input("Enter the second Number : "))
  print("""What do you want of these: 
  1 Addition
  2 Subtraction
  3 Multiplication
  4 Division
  5 Factorial
  6 Remainder
  7 Odd or Even
  8 Suare root """)
  user=input("Choose any one in above option : ")
  if (user=="1"):
    print(value_one+value_two)
  elif (user=="2"):
    print(value_one-value_two)
  elif (user=="3"):
    print(value_one*value_two)
  elif (user=="4"):
    print(value_one//value_two)
  elif (user=="5"):
    print(factorial(value_one))
    print(factorial(value_two))
  elif (user=="6"):
    print(value_one%value_two)
  elif (user=="7"):
    if value_one%value_two==0:
      print("Even")
    else:
      print("Odd")
  elif (user=="8"):
    print(squareroot(value_one))
    print(squareroot(value_two))
  else:
    print("Thank you")

advance_calculator()