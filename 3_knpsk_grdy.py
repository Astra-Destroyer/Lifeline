# Function to solve knapsack using greedy method (fractional knapsack)
def knapsack_greedy(weights, values, capacity):
    n = len(weights)
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    items.sort(reverse=True, key=lambda x: x[0])  # Sort by value-to-weight ratio

    total_value = 0
    total_weight = 0

    for ratio, weight, value in items:
        if total_weight + weight <= capacity:
            total_value += value
            total_weight += weight
        else:
            # Take fraction of the remaining weight
            remain = capacity - total_weight
            total_value += value * (remain / weight)
            total_weight += remain
            break

    return total_value, total_weight

# Function to display menu
def display_menu():
    print("\n--- Knapsack Problem Solver ---")
    print("1. Enter items and solve knapsack")
    print("2. Exit")
    return int(input("Enter your choice: "))

# Function to handle option 1
def option_1():
    n = int(input("Enter the number of items: "))
    weights = []
    values = []

    for i in range(n):
        weight = int(input(f"Enter weight of item {i+1}: "))
        value = int(input(f"Enter value of item {i+1}: "))
        weights.append(weight)
        values.append(value)

    capacity = int(input("Enter the knapsack capacity: "))
    
    total_value, total_weight = knapsack_greedy(weights, values, capacity)

    print(f"Maximum value that can be obtained: {total_value}")
    print(f"Total weight in the knapsack: {total_weight}")

# Main Program Loop
while True:
    choice = display_menu()

    if choice == 1:
        option_1()
    elif choice == 2:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
