Roll=[1,2,3,4,5,6]
print("Current Roll No List", Roll)
Val=int(input("Enter any Number "))
if Val in Roll:
    Roll.remove(Val)
    print(Roll)
else:
    print("Number is Not Present in List")
