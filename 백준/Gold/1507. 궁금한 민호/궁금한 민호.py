import sys

N = int(sys.stdin.readline())
cities = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = [[True for j in range(N)] for i in range(N)]

going = True
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j or i == k or j == k:
                continue
            if cities[j][k] == cities[j][i] + cities[i][k]:
                answer[j][k], answer[j][k] = False, False
            elif cities[j][k] > cities[j][i] + cities[i][k]:
                going = False

if going:
    result = 0
    for i in range(N):
        for j in range(i+1, N):
            if answer[i][j]:
                result += cities[i][j]
    print(result)
else:
    print(-1)