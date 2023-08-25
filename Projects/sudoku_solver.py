# Function to check if a move is valid in the Sudoku grid
def is_valid_move(grid, row, col, number):
    # Check if the number exists in the same row or column
    for x in range(9):
        if grid[row][x] == number or grid[x][col] == number:
            return False

    # Find the top-left corner of the 3x3 subgrid
    corner_row = row - row % 3
    corner_col = col - col % 3

    # Check if the number exists in the 3x3 subgrid
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False

    return True

# Function to solve the Sudoku grid using backtracking
def solve(grid, row, col):
    # If we have reached the last column, move to the next row
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    # If the cell is already filled, move to the next column
    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    # Try filling the cell with numbers 1 to 9
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            # Recursively solve the next cell
            if solve(grid, row, col + 1):
                return True
        grid[row][col] = 0  # If no valid number, backtrack

    return False

# Initial Sudoku grid with 0s indicating empty cells
grid = [[0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 9, 0, 0, 0, 0, 4, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 8],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0]]

# Call the solve function to find a solution
if solve(grid, 0, 0):
    # Print the solved Sudoku grid
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("No solution for this Sudoku.")
