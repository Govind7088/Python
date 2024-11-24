# Write mode.
 
f=open('another.txt', 'w')
f.write("Hyy Everyone This is Govind a software engineer")
f.close()


# Append mode.
f=open('another.txt', 'a')
f.write("I am pursuing in BCA")
f.close()

# Read mode.
f=open('another.txt','r')
data=f.read()
print(data)
f.close()