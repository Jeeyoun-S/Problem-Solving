def solution(m, n, puddles):
    answer = 0
    cur = [0, 0]
    
    board = [[0] * (m + 1) for _ in range(n + 1)]
    
    if m == 1 and puddles:
        return 0
    
    if n == 1 and puddles:
        return 0
    
    board[1][1] = 1
#     for i in range(1, m + 1):
#         board[1][i] = 1

#     for j in range(1, n + 1):
#         board[j][1] = 1
    
    for p in puddles:
        board[p[1]][p[0]] = -1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if board[j][i] != -1:
                if board[j - 1][i] != -1:
                    board[j][i] += board[j - 1][i]
                if board[j][i - 1] != -1:
                    board[j][i] += board[j][i - 1]
                
                board[n][m] %= 1000000007
    
    return board[n][m]