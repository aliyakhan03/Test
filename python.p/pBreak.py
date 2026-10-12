n = int(input("Enter Breaking Point"))
if n<=0 or n>10:
    print(f"Enter valid Range from 1 to Max 10")
for i in range (1,11):
  if i==n:
    print(f"Break Point{i}")
    break
  print(f"\n The Current Value = {i}")
