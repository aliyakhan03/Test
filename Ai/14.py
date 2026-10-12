def dfs(graph,node,search,visited):
    visited.append(node)
    if node == search:
        return True
    for next_node in graph[node]:
        if next_node not in visited:
            if dfs(graph, next_node, search,visited):
                return True
    return False
graph = {}
n = int(input("Enter number of vertices:"))
for i in range(n):
    v = input("Enter vertex:")
    graph[v] = input("Enter number of vertices:").split()
start=input("Enter starting vertex:")
search=input("Enter element to search:")
visited=[]
if dfs(graph, start, search, visited):
    print("DFS:",visited)
    print(search,"found at position",visited.index(search)+ 1)
else:
    print("DFS:",visited)
    print(search,"no found") 





