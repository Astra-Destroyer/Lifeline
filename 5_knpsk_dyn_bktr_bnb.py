# 0/1 Knapsack using Dynamic Programming
"""def knapsack_dp(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Example usage
n = int(input("Enter number of items: "))
weights = list(map(int, input(f"Enter the weights of {n} items: ").split()))
values = list(map(int, input(f"Enter the values of {n} items: ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))

result_dp = knapsack_dp(weights, values, capacity)
print(f"Maximum value using Dynamic Programming: {result_dp}")"""


# 0/1 Knapsack using Backtracking
"""def knapsack_backtrack(weights, values, capacity, n):
    def backtrack(i, curr_weight, curr_value):
        if i == n or curr_weight == capacity:
            return curr_value
        
        if weights[i] + curr_weight <= capacity:
            include_item = backtrack(i + 1, curr_weight + weights[i], curr_value + values[i])
        else:
            include_item = 0
        
        exclude_item = backtrack(i + 1, curr_weight, curr_value)
        
        return max(include_item, exclude_item)

    return backtrack(0, 0, 0)

# Example usage
n = int(input("Enter number of items: "))
weights = list(map(int, input(f"Enter the weights of {n} items: ").split()))
values = list(map(int, input(f"Enter the values of {n} items: ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))

result_backtrack = knapsack_backtrack(weights, values, capacity, n)
print(f"Maximum value using Backtracking: {result_backtrack}")
"""

import heapq

class Node:
    def __init__(self, level, value, weight, bound):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound

    def __lt__(self, other):
        return self.bound > other.bound  # for max heap

def bound(node, n, capacity, weights, values):
    if node.weight >= capacity:
        return 0
    profit_bound = node.value
    j = node.level + 1
    total_weight = node.weight

    while j < n and total_weight + weights[j] <= capacity:
        total_weight += weights[j]
        profit_bound += values[j]
        j += 1

    if j < n:
        profit_bound += (capacity - total_weight) * (values[j] / weights[j])

    return profit_bound

def knapsack_branch_and_bound(weights, values, capacity):
    n = len(values)
    # Sort items by value-to-weight ratio
    index = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
    weights = [weights[i] for i in index]
    values = [values[i] for i in index]

    max_value = 0
    queue = []

    v = Node(-1, 0, 0, 0)
    v.bound = bound(v, n, capacity, weights, values)
    heapq.heappush(queue, v)

    while queue:
        v = heapq.heappop(queue)

        if v.level == n - 1:
            continue

        u = Node(v.level + 1, v.value, v.weight, 0)

        # Check taking the current item
        u.weight = v.weight + weights[u.level]
        u.value = v.value + values[u.level]

        if u.weight <= capacity and u.value > max_value:
            max_value = u.value

        u.bound = bound(u, n, capacity, weights, values)

        if u.bound > max_value:
            heapq.heappush(queue, u)

        # Check without taking the current item
        u.weight = v.weight
        u.value = v.value
        u.bound = bound(u, n, capacity, weights, values)

        if u.bound > max_value:
            heapq.heappush(queue, u)

    return max_value

# Example usage
n = int(input("Enter number of items: "))
weights = list(map(int, input(f"Enter the weights of {n} items: ").split()))
values = list(map(int, input(f"Enter the values of {n} items: ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))

result_bb = knapsack_branch_and_bound(weights, values, capacity)
print(f"Maximum value using Branch and Bound: {result_bb}")
