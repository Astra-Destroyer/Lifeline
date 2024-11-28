def knapsack_greedy(weights, values, capacity):
    if len(weights) != len(values):
        raise ValueError("Weights and values lists must have the same length")

    n = len(weights)
    items = []

    for i in range(n):
        if weights[i] == 0:
            raise ValueError("Weight of an item cannot be zero")
        items.append((values[i] / weights[i], weights[i], values[i]))

    items.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    total_weight = 0

    for ratio, weight, value in items:
        if total_weight + weight <= capacity:
            total_value += value
            total_weight += weight
        else:
            remain = capacity - total_weight
            total_value += value * (remain / weight)
            total_weight += remain
            break

    return total_value, total_weight

def display_menu():
    print("\n--- Knapsack Problem Solver ---")
    print("1. Enter items and solve knapsack")
    print("2. Exit")
    return int(input("Enter your choice: "))

def option_1():
    while True:
        try:
            n = int(input("Enter the number of items: "))
            if n <= 0:
                print("Number of items must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    weights = []
    values = []

    for i in range(n):
        while True:
            try:
                weight = int(input(f"Enter weight of item {i+1}: "))
                if weight <= 0:
                    print("Weight must be a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

        while True:
            try:
                value = int(input(f"Enter value of item {i+1}: "))
                if value <= 0:
                    print("Value must be a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

        weights.append(weight)
        values.append(value)

    while True:
        try:
            capacity = int(input("Enter the knapsack capacity: "))
            if capacity <= 0:
                print("Capacity must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    try:
        total_value, total_weight = knapsack_greedy(weights, values, capacity)
        print(f"Maximum value that can be obtained: {total_value}")
        print(f"Total weight in the knapsack: {total_weight}")
    except ValueError as e:
        print(e)

while True:
    choice = display_menu()
    if choice == 1:
        option_1()
    elif choice == 2:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
