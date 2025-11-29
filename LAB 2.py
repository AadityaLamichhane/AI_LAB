#dfs-------------graph same as before

def dfs(graph, start, end, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()

    visited.add(start)

    if start == end:
        return path  # Found the end node

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, end, path + [neighbor], visited)
            if new_path:
                return new_path

    return None  # No path found

# Example graph as an adjacency list
graph = {
    
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']

}

start_node = 'A'
end_node = 'D'
path = dfs(graph, start_node, end_node)

if path:
    print("Path from", start_node, "to", end_node, ":", " -> ".join(path))
else:
    print("No path found from", start_node, "to", end_node)
