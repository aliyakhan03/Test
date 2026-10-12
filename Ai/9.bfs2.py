from collections import deque
def bfs(graph,start,goal):
    queue=deque([[start]])
    visitesd=set()
    while queue:
        path=queue.popleft()
        node=path[-1]
    if node==goal:
        return path
    if node is not visitesd:
        visitesd.add(node)
        for neighbor in graph[node]:
            new_p=path+[neighbor]
            queue.append(new_p)
            return None
graph = {
            'S':['A','B'],
               'A': ['C','D'],
               'B': [],
               'C': [],
               'D':[]
}
start='S'
goal='C'
result = bfs(graph, start, goal)
print("BFS path:", result)
