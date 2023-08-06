import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
parents = [i for i in range(N)]
locations = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
heap, total = [], 0

def find_parents(x):
    if parents[x] != x:
        parents[x] = find_parents(parents[x])
    return parents[x]

def union(x, y):
    if x > y:
        parents[x] = y
    else:
        parents[y] = x

for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    p_x, p_y = find_parents(X-1), find_parents(Y-1)
    if p_x != p_y:
        union(p_x, p_y)

# print(parents)
for i in range(N-1):
    for j in range(i+1, N):
        ix, iy = locations[i]
        jx, jy = locations[j]
        cost = ((ix - jx)**2 + (iy - jy)**2)**(1/2)
        heapq.heappush(heap, (cost, i, j))

# print(heap)
# print(parents)
# print(visited)

while heap:
    cost, x, y = heapq.heappop(heap)
    # print(cost, x, y)
    p_x, p_y = find_parents(x), find_parents(y)
    if p_x != p_y:
        union(p_x, p_y)
        total += cost

print('%.2f' % total)
# print(heap)
# print(parents)
# print(locations)