def bfs(graph, start):
    visited = []              # List of visited nodes
    queue = [start]           # FIFO queue for BFS
    cost = {start: 0}         # Distance from start node
    parent = {start: None}    # To trace paths

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(f"Visited: {node}, Cost: {cost[node]}")
            visited.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    cost[neighbor] = cost[node] + 1
                    parent[neighbor] = node

    print("\nVisited Order:", visited)
    print("Cost from Start:", cost)
    print("Parent Path Map:", parent)

# Define any graph (as a dictionary)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Call BFS with your graph and starting node
bfs(graph, 'A')
