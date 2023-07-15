def solution(n, results):
    
    games = [[0 for j in range(n+1)] for i in range(n+1)]
    for A, B in results:
        games[A][B] = 1
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if games[j][i] + games[i][k] == 2:
                    games[j][k] = 1
    
    answer = 0
    for i in range(1, n+1):
        total = 0
        for j in range(1, n+1):
            total += games[i][j]
            total += games[j][i]
        if total == n-1:
            answer += 1
    # print(answer)
    return answer