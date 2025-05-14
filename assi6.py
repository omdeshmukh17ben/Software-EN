
# variables = ['A', 'B', 'C', 'D']


# domains = {
#     'A': ['Red', 'Green', 'Blue'],
#     'B': ['Red', 'Green', 'Blue'],
#     'C': ['Red', 'Green', 'Blue'],
#     'D': ['Red', 'Green', 'Blue'],
# }


# neighbors = {
#     'A': ['B', 'C'],
#     'B': ['A', 'C', 'D'],
#     'C': ['A', 'B', 'D'],
#     'D': ['B', 'C']
# }


# def is_valid(assignment, var, value):
#     for neighbor in neighbors[var]:
#         if neighbor in assignment and assignment[neighbor] == value:
#             return False
#     return True


# def backtrack(assignment):
#     if len(assignment) == len(variables):
#         return assignment 

    
#     unassigned = [v for v in variables if v not in assignment]
#     var = unassigned[0]

#     for value in domains[var]:
#         if is_valid(assignment, var, value):
#             assignment[var] = value
#             result = backtrack(assignment)
#             if result:
#                 return result
#             del assignment[var]  

#     return None



# solution = backtrack({})
# print("Solution:", solution)
##################################################################
def generate_matrix(n):
    matrix = [[(i + j) % n + 1 for j in range(n)] for i in range(n)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        matrix = generate_matrix(n)
        print_matrix(matrix)
        print("Matrix generated successfully.")
#     print("Matrix generated successfully.")
#     print("Matrix generated successfully.")