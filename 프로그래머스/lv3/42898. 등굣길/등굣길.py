from collections import deque

def solution(m, n, puddles):

    delta = ((-1, 0), (0, -1))
    maps = [[0 for j in range(m)] for i in range(n)]
    maps[0][0] = 1
    
    for x in range(n):
        for y in range(m):
            if [y+1, x+1] in puddles:
                maps[x][y] = 0
                continue
            for dx, dy in delta:
                xx, yy = x+dx, y+dy
                if 0 <= xx < n and 0 <= yy < m:
                    maps[x][y] = (maps[x][y] + maps[xx][yy]) % 1000000007
            # print(x, y, maps)
                
    print(maps)
    return maps[n-1][m-1]