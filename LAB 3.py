#WAP to implement uniform cost search in python

import heapq

def ucs(graph, start, end):
    # Priority queue: (cumulative_cost, current_node, path_to_node)
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, current, path = heapq.heappop(queue)

        if current == end:
            return cost, path  # Found the goal node

        if current in visited:
            continue

        visited.add(current)

        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

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

start_node = 'A'
end_node = 'D'
cost, path = ucs(graph, start_node, end_node)

if path:
    print(f"Lowest-cost path from {start_node} to {end_node}: {' -> '.join(path)} (Cost: {cost})")
else:
    print(f"No path found from {start_node} to {end_node}")
