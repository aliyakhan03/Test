print("Program for Best first Search")
print("*"*34)
graph={
    'S':['A','C'],
    'A':['D','E'],
    'B':['F'],
    'C':['G'],
    'D':['G'],
    'E':[]
    'F':
    'H':
    'G':
}
h={
    'A':6,
    'B':5,
    'C':7,
    'E':2,
    'F':3,
    'G':0
}
start=input("\t\t\t Enter Start:")
goal=input("\t\t\t Enter Goal:")
open=[start]
while open:
    node=min(open,key=lambda x:h[x])
    open.remove(node)
    print(node, end="")
    if node==goal:
        print("\n Goal Found...........")
        break
    for x in graph[node]:
        open.append(x)
