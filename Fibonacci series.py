def fibonacci_series(n):
    a = int(input("Enter the First number : "))
    b = int(input("Enter the Second number : "))
    for i in range(0,n):
       c = a + b
       a = b
       b = c
       print(c)
fibonacci_series(10)