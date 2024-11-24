# print item with index.

list1=[3, 6, 53, False, "Govind", 7.5]

# index=0
# for item in  list1:
#   print(item, index)
#   index +=1

for index, item in enumerate(list1):
  print(item, index)