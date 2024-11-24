f=open('sample.txt','r')

data=f.readline() # Read the first line of file.
print(data)

data=f.readline() # Read the second line of file.
print(data)

data=f.readline() # Read the third line of file.....and so on....
print(data)
f.close()