myDict={ 
  "name":"Is the good boy",
  "govind":"Web developer",
  "marks":[2, 5, 8],
  "anotherdict":{"govind":"Engineer"}, # Nested Dictionary.
  1:5
}
#print(myDict.keys()) # print the keys of dictionary.
#print(myDict.values()) #print the values of dictionary.
#print(myDict.items()) # print the keys with values of dictionary.
print(myDict)

# Add the any new keys and value with help of update function.
'''updateDict={
  "lovish":"Friend",
  "divya":"Friend",
  "saras":"Friend"
}
myDict.update(updateDict)
print(myDict)'''

print(myDict.get("name"))
print(myDict["name"])  

# different betweeb get and [] syntax.