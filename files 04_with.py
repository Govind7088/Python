# with function.

with open('another.txt','r') as f:
  a=f.read()
print(a)

with open('another.txt','w') as f:
  a=f.write("This is Govind")
print(a)