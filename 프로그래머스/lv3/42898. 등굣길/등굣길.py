from collections import deque

def solution(m, n, puddles):
    
    delta = ((-1, 0), (0, -1)) # 이동할 위치
    maps = [[0 for j in range(m)] for i in range(n)] # 지도
    maps[0][0] = 1 # 집에서 출발
    
    # 1행 1열 -> 1행 2열 -> ... -> 2행 1열 순으로 반복
    for x in range(n):
        for y in range(m):
            if [y+1, x+1] in puddles: # 웅덩이가 있다면
                continue
            # 위와 왼쪽에 값이 있다면 더해주기
            for dx, dy in delta:
                xx, yy = x+dx, y+dy
                if 0 <= xx < n and 0 <= yy < m:
                    maps[x][y] = (maps[x][y] + maps[xx][yy]) % 1000000007
    return maps[n-1][m-1]