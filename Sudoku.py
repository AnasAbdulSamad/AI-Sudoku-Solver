
sudoku_board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def find_empty(board):
    "Function used to determine an empty box in sudoku puzzle"
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None


def valid(board, match, position):
    "Checks for valid position for row, coloumn and block"
    # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == match and position[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == match and position[0] != i:
            return False

    # Check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == match and (i,j) != position:
                return False

    return True


def solve(board):
    solution = find_empty(board)
    if not solution:
        return True
    else:
        row, coloumn = solution

    for i in range(1,10):
        if valid(board, i, (row, coloumn)):
            board[row][coloumn] = i

            if solve(board):
                return True

            board[row][coloumn] = 0

    return False




def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------------------------- ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")





print("="*100)
print("\t\t\t\t\tSUDOKU SOLVER")
print("="*100)
print()
print("~"*100)

print()
print("UNSOLVED BOARD")
print()


print_board(sudoku_board)
solve(sudoku_board)
print()
print("SOLVED BOARD")
print()
print_board(sudoku_board)
