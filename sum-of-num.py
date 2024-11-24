def sum(n):
  if n==0 or n==1:
    return 1
  return n+sum(n-1)
num=int(input("Enter your Number\n"))
print(sum(num))