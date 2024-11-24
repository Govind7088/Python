a=10  # Here, it is Global Function.
def func1():
  a=8 # Here, it is Local Function.
  print(a)
func1()
print(a)