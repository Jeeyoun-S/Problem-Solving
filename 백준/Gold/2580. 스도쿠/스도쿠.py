import sys

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
empty = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            empty.append([i, j])

def find_row(row, n):
    for col in range(9):
        if n == sudoku[row][col]:
            return False
    return True

def find_column(col, n):
    for row in range(9):
        if n == sudoku[row][col]:
            return False
    return True

def find_square(row, col, n):
    for i in range(3):
        for j in range(3):
            if n == sudoku[row//3 * 3 + i][col//3 * 3 + j]:
                return False
    return True

def backtracking(n):
    if n == len(empty):
        for s in sudoku:
            print(*s)
        exit()

    for i in range(1, 10):
        x, y = empty[n][0], empty[n][1]
        if find_row(x, i) and find_column(y, i) and find_square(x, y, i):
            sudoku[x][y] = i
            backtracking(n+1)
            sudoku[x][y] = 0

backtracking(0)