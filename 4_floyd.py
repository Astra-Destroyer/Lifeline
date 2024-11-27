INF = float('inf')  # A value to represent infinity for unreachable paths

def floyd_warshall(graph, V):
    # Initialize the solution matrix same as input graph matrix
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]

    # Floyd-Warshall Algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def print_matrix(matrix, cities):
    print(f"\t{' '.join(cities)}")
    for i in range(len(matrix)):
        print(f"{cities[i]}\t", end="")
        for j in range(len(matrix)):
            if matrix[i][j] == INF:
                print("INF", end="\t")
            else:
                print(matrix[i][j], end="\t")
        print()

# User Input
V = int(input("Enter the number of cities: "))
cities = []
print("Enter the names of the cities:")
for _ in range(V):
    city = input()
    cities.append(city)

# Initialize adjacency matrix with INF, 0 on the diagonal
graph = [[INF if i != j else 0 for j in range(V)] for i in range(V)]

E = int(input("Enter the number of flights (edges): "))
print("Enter the flight details (source, destination, distance):")
for _ in range(E):
    source, destination, distance = input().split()
    distance = int(distance)
    
    # Get the indices of the cities
    u = cities.index(source)
    v = cities.index(destination)
    
    # Update the graph
    graph[u][v] = distance

# Display the Adjacency Matrix
print("\nAdjacency Matrix:")
print_matrix(graph, cities)

# Run Floyd-Warshall Algorithm
shortest_paths = floyd_warshall(graph, V)

# Display the Shortest Path Matrix
print("\nShortest Path Matrix:")
print_matrix(shortest_paths, cities)
