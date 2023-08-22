import sys
from itertools import combinations
from collections import deque

sys.setrecursionlimit(1000000)
N, M, D = map(int, sys.stdin.readline().split())
locations = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
delta = ((0, -1), (-1, 0), (0, 1))
result = 0
enemy = sum([locations[i].count(1) for i in range(N)])


def go():
    last_row = locations[-1][:]
    num = last_row.count(1)
    # print("num", num)
    for i in range(N-2, -1, -1):
        locations[i+1] = locations[i][:]
    locations[0] = [0 for _ in range(M)]

    for i in range(N):
        for j in range(M):
            if locations[i][j] < 0:
                locations[i][j] = 0

    return [last_row, num]

def back(last_row):
    for i in range(0, N-1):
        locations[i] = locations[i+1][:]
    locations[-1] = last_row
    # print("복구", locations)
    return

def attack(idx, points, total, enemies):
    global locations
    # print("attack", enemies)
    # print(idx, points, total)
    # for location in locations:
    #     print(location)
    # print(locations)
    if idx >= len(points) or enemies <= 0:
        if enemies <= 0:
            global result
            result = max(result, total)
            # print("result", result, "total", total)
        else:
            # print("---------------------------")
            # print(locations)
            # print("1111111111111")
            last_row, num = go()
            # print(locations, last_row)
            attack(0, points, total, enemies-num)
            # print("2222222222222")
            back(last_row)
            # print(locations)
            # print("---------------------------")
        return

    visited = [[False for j in range(M)] for i in range(N)]
    queue = deque()
    queue.append((N, points[idx]))

    while queue:
        x, y = queue.popleft()
        # print(x, y, abs(x-N) + abs(y-points[idx]))

        if abs(x-N) + abs(y-points[idx]) >= D:
            continue

        for dx, dy in delta:
            xx, yy = x+dx, y+dy
            # print("xx", xx, "yy", yy)
            if 0 <= xx < N and 0 <= yy < M and not visited[xx][yy]:
                # print(">>>>>")
                if abs(locations[xx][yy]) == 1:
                    if locations[xx][yy] < 0:
                        attack(idx+1, points, total, enemies)
                    else:
                        locations[xx][yy] = -1
                        attack(idx+1, points, total+1, enemies-1)
                    locations[xx][yy] = 1
                    return

                visited[xx][yy] = True
                queue.append((xx, yy))

    attack(idx+1, points, total, enemies)
    return


for points in combinations(range(M), 3):
    # print("start", enemy)
    attack(0, points, 0, enemy)

print(result)