import sys
from collections import deque

N, M, T = map(int, sys.stdin.readline().split())
castle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))

visited = [[False for j in range(M)] for i in range(N)]
visited[0][0] = True

queue = deque()
queue.append((0, 0, 0))

min_result = sys.maxsize

while queue:
    x, y, time = queue.popleft()
    # print(x, y, time)

    if x == N-1 and y == M-1:
        min_result = min(time, min_result)
        continue

    for dx, dy in delta:
        xx, yy = x+dx, y+dy
        if 0 <= xx < N and 0 <= yy < M and not visited[xx][yy]:
            if castle[xx][yy] == 0:
                visited[xx][yy] = True
                queue.append((xx, yy, time+1))
            elif castle[xx][yy] == 2:
                visited[xx][yy] = True
                time += abs(xx - N + 1) + abs(yy - M + 1)
                queue.append((N-1, M-1, time+1))

if min_result == sys.maxsize or min_result > T:
    print("Fail")
else:
    print(min_result)