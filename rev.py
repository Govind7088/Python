# def comapreValue(a, b):
#   return a if(a>b) else b
# a,b =5,1
# print(comapreValue(a, b))

'''
a = 20
b = 6
res = a/b
print(res)
'''
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
print("Before swapping numbers are : ", num1, num2)
temp = num1
num1 = num2
num2 = temp
print("After swapping numbers are : ", num1, num2)
