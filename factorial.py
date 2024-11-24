# For direct get the Answer.
'''
n=5
a=1
for i in range(n):
  a=a*(i+1)
print(a)

# For Serial number by answer.
n=5
a=1
for i in range(n):
  a=a*(i+1)
  print(a)
  
'''
'''
def factorail(n):
  a=1
  for i in range(n):
    a=a*(i+1)
  return a
f=int(input("Enter the Number: "))
print(factorail(f))

'''
def factorial_recursive(n):
  if n==1 or n==0:
    return 1
  return n*factorial_recursive(n-1)
f=int(input("Enter your number : "))
print(factorial_recursive(f))