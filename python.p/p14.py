def larg(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
num1=float(input("Enter Number 1:"))
num2=float(input("Enter Number 2:"))
num3=larg(num1,num2)
print(f"The largest Number is:{num3}")
