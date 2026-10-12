import math
num = int(input("Enter N"))
if num<=0:
    print("Invalid ;")
else:
    res=math.factorial(num)
    print(f"Factorial of {num} is {res}")