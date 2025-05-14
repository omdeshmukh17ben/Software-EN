
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def generate_permutations(cities, start=0, result=[]):
    if start == len(cities) - 1:
        result.append(cities[:])
        return
    for i in range(start, len(cities)):
        cities[start], cities[i] = cities[i], cities[start]  
        generate_permutations(cities, start + 1, result)
        cities[start], cities[i] = cities[i], cities[start]  

cities = [1, 2, 3]  
all_paths = []
generate_permutations(cities, 0, all_paths)


min_distance = float('inf')
shortest_path = []

for path in all_paths:
    full_path = [0] + path + [0]  
    total = 0
    for i in range(len(full_path) - 1):
        total += distance[full_path[i]][full_path[i + 1]]
    if total < min_distance:
        min_distance = total
        shortest_path = full_path


print("Shortest path:", shortest_path)
print("Minimum distance:", min_distance)
