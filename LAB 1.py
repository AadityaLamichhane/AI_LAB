
from collections import deque
def bfs(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])  
    while queue:
        current, path = queue.popleft()
        
        if current == end:
            return path  

        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    
    return None  
graph = {
    'A': ['I', 'G'],
    'B': ['C', 'D','E'],
    'C': ['B','G','F'],
    'D': ['E','B'],
    'E': ['B','D','H'],
    'F': ['H','C'],
    'G': ['A','C'],
    'H': ['E','F'],
    'I': ['A']
}

start_node = 'A'
end_node = 'F'
path = bfs(graph, start_node, end_node)

if path:
    print(" Using BF Path from ", start_node, "to", end_node, ":", " -> ".join(path))
    print("Aaditya lamichhane Lab Q1 ")
else:
    print("No path found from", start_node, "to", end_node)
