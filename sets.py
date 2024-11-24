a={1, 3, 4, 5, 1}
print(type(a))
print(a)

# This set make an empty dictionary and not make an empty sets.
#a={}
#print(type(a))
 
# An empty sets maked this below syntax.
b=set()
print(type(b))
b.add(2)
b.add(4)
b.add(6)
b.add(6)
b.add((2, 4, 6))
print(b)

print(len(b))

b.remove(6)
print(b)

print(b.pop())
print(b)
