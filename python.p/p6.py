a = int(input("Enter the value a:"))
b = int(input("Enter the value b: "))

Addition = a+b
substraction = a-b
Multipication = a*b

if b!=0:
  Division=a/b
else:
  print("Invalid Number")
  Division = "Not possible"
  
print(f"The Addition of {a}+{b} is:{Addition}")
print(f"The substraction of {a}-{b} is:{substraction}")
print(f"The Multipication of {a}*{b} is:{Multipication}")
print(f"The Division of {a}/{b} is:{Division}")

