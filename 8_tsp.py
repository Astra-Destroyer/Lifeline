import sys

# Menu-driven function
def tsp_menu():
    print("Menu:")
    print("1. Solve TSP using Branch and Bound")
    print("2. Solve TSP using Dynamic Programming (Held-Karp Algorithm)")
    print("3. Exit")
    
    while True:
        choice = int(input("\nEnter your choice (1/2/3): "))
        if choice == 1:
            tsp_branch_and_bound()
        elif choice == 2:
            tsp_dynamic_programming()
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Utility function to print a matrix (for debugging purposes)
def print_matrix(matrix):
    for row in matrix:
        print(row)
        
##################################################
# Branch and Bound Approach for TSP
##################################################
class TSPSolverBB:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        self.min_cost = sys.maxsize
        self.final_path = []
    
    def tsp_util(self, current_path, current_bound, current_weight, level, visited):
        if level == self.n:
            if self.graph[current_path[level - 1]][current_path[0]] != 0:
                current_res = current_weight + self.graph[current_path[level - 1]][current_path[0]]
                if current_res < self.min_cost:
                    self.min_cost = current_res
                    self.final_path = current_path[:]
            return

        for i in range(self.n):
            if self.graph[current_path[level - 1]][i] != 0 and not visited[i]:
                temp_bound = current_bound
                current_weight += self.graph[current_path[level - 1]][i]

                if level == 1:
                    current_bound -= (self.first_min(current_path[level - 1]) + self.first_min(i)) / 2
                else:
                    current_bound -= (self.second_min(current_path[level - 1]) + self.first_min(i)) / 2

                if current_bound + current_weight < self.min_cost:
                    visited[i] = True
                    current_path[level] = i

                    self.tsp_util(current_path, current_bound, current_weight, level + 1, visited)

                current_weight -= self.graph[current_path[level - 1]][i]
                current_bound = temp_bound

                visited[i] = False

    def first_min(self, i):
        min_val = sys.maxsize
        for k in range(self.n):
            if self.graph[i][k] != 0 and self.graph[i][k] < min_val:
                min_val = self.graph[i][k]
        return min_val

    def second_min(self, i):
        first, second = sys.maxsize, sys.maxsize
        for j in range(self.n):
            if self.graph[i][j] != 0:
                if self.graph[i][j] <= first:
                    second = first
                    first = self.graph[i][j]
                elif self.graph[i][j] < second:
                    second = self.graph[i][j]
        return second

    def tsp(self):
        current_path = [-1] * (self.n + 1)
        visited = [False] * self.n

        current_bound = 0
        for i in range(self.n):
            current_bound += (self.first_min(i) + self.second_min(i))
        current_bound = current_bound / 2

        visited[0] = True
        current_path[0] = 0

        self.tsp_util(current_path, current_bound, 0, 1, visited)

        print(f"Optimal cost using Branch and Bound: {self.min_cost}")
        print(f"Path: {self.final_path + [self.final_path[0]]}")

def tsp_branch_and_bound():
    n = int(input("\nEnter the number of cities: "))
    graph = []
    print("Enter the distance matrix (use 0 for no connection between cities):")
    for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        graph.append(row)

    solver = TSPSolverBB(graph)
    solver.tsp()

##################################################
# Dynamic Programming Approach for TSP (Held-Karp Algorithm)
##################################################
def tsp_dynamic_programming():
    n = int(input("\nEnter the number of cities: "))
    graph = []
    print("Enter the distance matrix (use 0 for no connection between cities):")
    for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        graph.append(row)

    def tsp_dp(graph, n):
        dp = [[sys.maxsize] * (1 << n) for _ in range(n)]
        dp[0][1] = 0  # Starting from city 0

        for mask in range(1 << n):  # Iterate over all subsets of cities
            for u in range(n):
                if mask & (1 << u):  # If city u is in the current subset
                    for v in range(n):
                        if mask & (1 << v) and u != v:  # City v is also in the subset and v != u
                            dp[u][mask] = min(dp[u][mask], dp[v][mask ^ (1 << u)] + graph[v][u])

        return min(dp[i][(1 << n) - 1] + graph[i][0] for i in range(1, n))

    result = tsp_dp(graph, n)
    print(f"Optimal cost using Dynamic Programming: {result}")

# Run the menu-driven program
tsp_menu()
