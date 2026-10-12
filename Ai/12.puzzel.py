from collections import deque
start=input("Enter Starting Puzzel")
goal=input("Enter your Puzzel")
queue=deque([(start,[start])])
visted=[start]
moves={
    0:[1,3],
}