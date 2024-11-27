import time
import random
import matplotlib.pyplot as plt

# Quick Sort Function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Function to measure execution time
def measure_execution_time(arr):
    start_time = time.time()
    sorted_arr = quick_sort(arr)
    end_time = time.time()
    return sorted_arr, end_time - start_time

# Function to display the menu
def display_menu():
    print("\n--- Quick Sort Program ---")
    print("1. Generate random array and sort")
    print("2. Compare execution times for multiple input sizes")
    print("3. Exit")
    return int(input("Enter your choice: "))

# Function to handle option 1
def option_1():
    array_size = int(input("Enter the size of the array: "))
    arr = random.sample(range(1, array_size * 10), array_size)
    print(f"Generated array: {arr}")
    
    sorted_arr, exec_time = measure_execution_time(arr)
    print(f"Sorted array: {sorted_arr}")
    print(f"Execution Time: {exec_time:.6f} seconds")

# Function to handle option 2
def option_2():
    input_sizes = list(map(int, input("Enter array sizes separated by space (e.g., 100 500 1000): ").split()))
    execution_times = []

    for size in input_sizes:
        arr = random.sample(range(1, size * 10), size)
        _, exec_time = measure_execution_time(arr)
        execution_times.append(exec_time)
        print(f"Array Size: {size}, Execution Time: {exec_time:.6f} seconds")

    # Plotting the results
    plt.plot(input_sizes, execution_times, marker='o')
    plt.title('Quick Sort Execution Time Analysis')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()

# Main Program Loop
while True:
    choice = display_menu()

    if choice == 1:
        option_1()
    elif choice == 2:
        option_2()
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
