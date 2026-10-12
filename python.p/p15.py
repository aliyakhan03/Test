def larg(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            num4=num1
        else:
            num4=num3
    else:
        if num2>num3:
            num4=num2
        else:
            num4=num3
            return num4
num1=float(input("Enter the n1:"))
num2=float(input("Enter the n2:"))
num3=float(input("Enter the n3:"))
res=larg(num1, num2, num3)
print(f"The largest number is: {res}")
