def factorial(num):
  if num == 0:
    return 1
  else:
    return num*factorial(num-1)
print(factorial(10))

# num1 = int(input("Enter your number : "))
# print(factorial(num1))