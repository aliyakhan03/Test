graph = {
    'S': {'A':1, 'G': 10},
    'A': {'B':2, 'C':1},
    'C': {'D':3, 'G':4},
    'G': {''}
}

h = {'A':3, 'B':4, 'C':2, 'D':6, 'G':0}
start = input("Enter start node:")
goal = input("Enter goal node:")
open_list = [start]
cost = {start:0}
path = {start: None}

while open_list:
    open_list.sort(key=lambda x: cost[x] + h[x])
    node = open_list.pop(0)
    if node == goal:
        break
    for next_node in graph[node]:
        new_cost = cost[node]+ graph[node][next_node]
        if next_node not in cost or new_cost < cost[next_node]:
            cost[next_node]= new_cost
            path[next_node]= node
            open_list.append(next_node)
        if node == goal:
            result = []
            while node is None:
                result.append(node)
                node = path[node]
                print("Optimal path:", result[::-1])
                print("Total cost:",cost[goal])
            else:
                print("path not found")