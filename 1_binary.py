import random

# Global variable to store the list
un_list = []

# Function to generate a list of random integers
def generate_list(size):
    global un_list
    un_list = [random.randint(1, 5000) for _ in range(size)]
    print("List generated.")
    print("Unsorted list (first 500 elements):", un_list[:500])

# Merge sort function
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1

    sorted_arr.extend(left[left_index:])
    sorted_arr.extend(right[right_index:])

    return sorted_arr

# Binary search function that returns all indices of the key
def binary_search_all_indices(sorted_list, key):
    indices = []
    
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_list[mid] == key:
            # Found an occurrence of the key, now find all occurrences
            # Search left of mid
            left_index = mid
            while left_index >= 0 and sorted_list[left_index] == key:
                indices.append(left_index)
                left_index -= 1
            
            # Search right of mid
            right_index = mid + 1
            while right_index < len(sorted_list) and sorted_list[right_index] == key:
                indices.append(right_index)
                right_index += 1

            indices.sort()
            return indices
        elif sorted_list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return indices

# Function to display the menu
def display_menu():
    print("\nMenu:")
    print("1. Generate a new list")
    print("2. Sort the list")
    print("3. Search for a key in the sorted list")
    print("4. Exit")

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        size = int(input("Enter the size of the list to generate: "))
        generate_list(size)
    
    elif choice == "2":
        if un_list:
            sorted_list = merge_sort(un_list)
            print("List sorted.")
            print("Sorted list (first 500 elements):", sorted_list[:500])
        else:
            print("The list has not been generated yet. Please generate a list first.")
    
    elif choice == "3":
        if un_list:
            sorted_list = merge_sort(un_list)
            key = int(input("Enter key to search: "))
            indices = binary_search_all_indices(sorted_list, key)
            if indices:
                print(f"Element {key} found at indices {indices}.")
            else:
                print(f"Element {key} not found in the list.")
        else:
            print("The list has not been generated yet. Please generate a list first.")
    
    elif choice == "4":
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please enter a valid option.")

