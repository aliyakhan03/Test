from collections import deque
graph = {
    'S': ['A','B'],
    'A': ['C','D'],
    'B': ['G','H'],
    'C': ['E','F'],
    'D': [],
    'G': ['I'],
    'H': [],
    'E': ['F'],
    'K': []
}
visited=[]
queue=deque(['S'])
while queue:
    node=queue.popleft()
    if node is not visited:
        print(node, end="")
        visited.append(node)
        for neighbour in graph[node]:
            queue.append(neighbour)