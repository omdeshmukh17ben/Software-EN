from collections import deque

def is_goal(state, target):
    return state[0] == target or state[1] == target

def get_next_states(current, cap_a, cap_b):
    a, b = current
    states = []

    # Fill jug A
    states.append((cap_a, b))
    # Fill jug B
    states.append((a, cap_b))
    # Empty jug A
    states.append((0, b))
    # Empty jug B
    states.append((a, 0))
    # Pour A -> B
    pour = min(a, cap_b - b)
    states.append((a - pour, b + pour))
    # Pour B -> A
    pour = min(b, cap_a - a)
    states.append((a + pour, b - pour))

    return states

def water_jug_solver(cap_a, cap_b, target):
    visited = set()
    queue = deque()
    queue.append(((0, 0), []))  # (state, path)

    while queue:
        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if is_goal((a, b), target):
            return path

        for state in get_next_states((a, b), cap_a, cap_b):
            if state not in visited:
                queue.append((state, path))

    return None

# Example: Jug A = 4L, Jug B = 3L, Target = 2L
solution = water_jug_solver(4, 3, 2)

if solution:
    print("Steps to reach target:")
    for i, (a, b) in enumerate(solution):
        print(f"Step {i}: Jug A = {a}L, Jug B = {b}L")
else:
    print("No solution found.")
 