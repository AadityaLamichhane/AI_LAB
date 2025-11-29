# WAP to implement greedy search in python, GRAPH SAME AS 1 AND 2, LATER heuristic values are inserted by myself

import heapq

def greedy_search(graph, heuristics, start, end):
    # Priority queue: (heuristic, current_node, path_to_node)
    queue = [(heuristics[start], start, [start])]
    visited = set()

    while queue:
        h, current, path = heapq.heappop(queue)

        if current == end:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(queue, (heuristics[neighbor], neighbor, path + [neighbor]))

    return None

# Example graph (unweighted edges)
graph = {
    'A': ['B', 'G'],
    'B': ['G', 'C'],
    'C': [],
    'G': ['E'],
    'E': ['J','K'],
    'J': ['F','D'],
    'F': [],
    'K': ['D'],
    'D': ['J']
}

# Heuristic values (estimated cost from each node to the goal 'F')
heuristics = {
    'A': 9,
    'B': 7,
    'C': 9,
    'D': 3,
    'E': 3,
    'F': 0,
    'G':5,
    'J':2,
    'K':5
}

start_node = 'A'
end_node = 'D'
path = greedy_search(graph, heuristics, start_node, end_node)

if path:
    print(f"Greedy path from {start_node} to {end_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {end_node}")
