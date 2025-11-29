from collections import deque

def water_jug_problem():
    visited = set()
    queue = deque()

    
    queue.append((0, 0, [(0, 0, "Start")]))  # include start
    visited.add((0, 0))

    while queue:
        a, b, path = queue.popleft()

        # Goal: 4L in jug1
        if a == 4:
            path.append((a, b, "Goal Reached"))
            # Print path without steps
            for x, y, action in path[1:]:  # skip start
                print(f"jug1 = {x}L, jug2 = {y}L   {action}")
            return

        # Capacities: jug1=7L, jug2=5L
        next_states = {
            (7, b): "Fill jug1 ",
            (a, 5): "Fill jug2 ",
            (0, b): "Empty jug1 ",
            (a, 0): "Empty jug2 ",
            (min(a + b, 7), b - (min(a + b, 7) - a)): " jug2 to jug1",
            (a - (min(a + b, 5) - b), min(a + b, 5)): "jug1 to jug2"
        }

        for state, desc in next_states.items():
            if state not in visited:
                visited.add(state)
                queue.append((state[0], state[1], path + [(state[0], state[1], desc)]))

water_jug_problem()
