import random
import math


dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]


def path_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += dist[path[i]][path[i + 1]]
    return cost

def swap_two(path):
    a = random.randint(1, len(path) - 2) 
    b = random.randint(1, len(path) - 2)
    while a == b:
        b = random.randint(1, len(path) - 2)
    new_path = path[:]
    new_path[a], new_path[b] = new_path[b], new_path[a]
    return new_path


def simulated_annealing():
    current = [0, 1, 2, 3, 0]  
    current_cost = path_cost(current)

    T = 1000      
    cooling = 0.99 

    best = current[:]
    best_cost = current_cost

    while T > 1:
        new = swap_two(current)
        new_cost = path_cost(new)

        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
            current = new
            current_cost = new_cost

        if current_cost < best_cost:
            best = current[:]
            best_cost = current_cost

        T = T * cooling  

    return best, best_cost

# Run it
best_path, best_cost = simulated_annealing()
print("Best path:", best_path)
print("Cost:", best_cost)
