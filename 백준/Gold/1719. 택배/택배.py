import sys

n, m = map(int, sys.stdin.readline().split())
roads = [[(sys.maxsize, 0) for j in range(n)] for i in range(n)]
for _ in range(m):
    A, B, time = map(int, sys.stdin.readline().split())
    roads[A-1][B-1], roads[B-1][A-1] = (time, B), (time, A)

for i in range(n):
    for j in range(n):
        for k in range(n):
            cost = roads[j][i][0] + roads[i][k][0]
            # print("-------------------------------")
            # print(f'{j}에서 {k}까지 현재 {roads[j][k]}')
            # print(f'{j}에서 {i}까지 현재 {roads[j][i]}')
            # print(f'{i}에서 {k}까지 현재 {roads[i][k]}')
            if roads[j][k][0] > cost:
                roads[j][k] = (cost, roads[j][i][1])

for i in range(n):
    for j in range(n):
        roads[i][j] = '-' if i == j else roads[i][j][1]

for road in roads:
    print(*road)