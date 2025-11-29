import heapq

def a_star_search(graph, heuristics, start, end):
    # Priority queue: (f = g + h, g, current_node, path)
    queue = [(heuristics[start], 0, start, [start])]
    visited = set()

    while queue:
        f, g, current, path = heapq.heappop(queue)

        if current == end:
            return g, path

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(queue, (new_f, new_g, neighbor, path + [neighbor]))

    return None, None  # No path found

# Example weighted graph (adjacency list with weights)
graph = {
    'A': [('B', 3), ('D', 14)],
    'B': [('D', 10), ('C', 4)],
    'C': [('D', 5)],
    'D': [('E',2),('F',1)],
    'E': [],
    'F': []
}

# Heuristic values (estimated cost from each node to the goal 'F')
heuristics = {
    'A': 9,
    'B': 7,
    'C': 9,
    'D': 3,
    'E': 3,
    'F': 0
}

start_node = 'A'
end_node = 'D'
cost, path = a_star_search(graph, heuristics, start_node, end_node)

if path:
    print(f"A* path from {start_node} to {end_node}: {' -> '.join(path)} (Cost: {cost})")
else:
    print(f"No path found from {start_node} to {end_node}")
