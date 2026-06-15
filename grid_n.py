N = 4

board = [[0 for _ in range(N)] for _ in range(N)]

def is_safe(board, row, col):
    # Check left side of row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueen(board, col):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_nqueen(board, col + 1):
                return True

            board[i][col] = 0

    return False


if solve_nqueen(board, 0):
    print("Solution Found:")
    for row in board:
        print(row)
else:
    print("No Solution")
