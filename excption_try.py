while(True):
  print("Press q to quit")
  a = input("Enter a Number: ")
  if a=='q':
    break
     try:
       a = int(a)
       if a>6:
         print("You Enter the number graterthan 6")
print("Thanks for playing this game!")