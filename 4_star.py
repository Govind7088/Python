num=4
for i in range(4):
  print("*"*(i+1))


num=3
for i in range(3):
  print(" "*(num-i-1), end="")
  print("*"*(2*i+1), end="")
  print(" "*(num-i-1))
