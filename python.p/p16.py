def check (num):
    if num>0:
        return "Positive"
    elif num<0:
        return "Negative"
    else:
        return "Zero"
num1 = float(input("Enter the number:"))
num2 = float(input("Enter the numbr:"))
res1 = check(num1)
res2 = check(num2)
print(f"The number is {res1}:{num1}")
print(f"The number is {res2}:{num2}")



    