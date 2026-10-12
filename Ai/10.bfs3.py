from collections import deque
elements=input("Enter Graph Elements").split()
graph{}
for element in elements:
    neighbours=input("Enter Neighbours of " + element":").split()
    graph[element]=neighbours 
    search=input("Enter Element to search:")
    queue=deque([element[0]])
    visited=[]
    position=0
    found=False
    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.append(node)
            position+=1
            if node == found:
                found=True
                break
            for neighbour in graph(node):
                if neighbour not in visited:
                   queue.append(neighbour)
                   if found:
                      print("Element Found:", search)
                      print("Position is:", position)
                else:
                    print("Element not Found")