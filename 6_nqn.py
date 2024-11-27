# Function to check if placing a queen at board[row][col] is safe
def is_safe(board, row, col, N):
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper diagonal on the right
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

# Function to solve N-Queens using backtracking and store all solutions
def solve_nqueens(board, row, N, solutions):
    # Base case: All queens are placed
    if row >= N:
        solutions.append([row[:] for row in board])  # Store a copy of the board
        return

    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen
            board[row][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens(board, row + 1, N, solutions)

            # Backtrack by removing the queen
            board[row][col] = 0

# Function to print a solution board
def print_board(board, N):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print("\n")  # Print a new line between different solutions

# Main function to take user input and solve the problem
def n_queens():
    N = int(input("Enter the value of N for the N-Queens problem: "))
    
    # Initialize the board with 0s
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    # List to store all solutions
    solutions = []

    # Find all solutions
    solve_nqueens(board, 0, N, solutions)

    # If solutions exist, print them
    if solutions:
        print(f"\nTotal solutions for {N}-Queens problem: {len(solutions)}")
        for i, solution in enumerate(solutions):
            print(f"\nSolution {i + 1}:")
            print_board(solution, N)
    else:
        print(f"No solution exists for {N}-Queens problem.")

# Run the program
n_queens()
 