import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
edges = []
distance = [sys.maxsize for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((A-1, B-1, C))

distance[0] = 0
for i in range(N):
    for A, B, C in edges:
        if distance[A] < sys.maxsize and distance[B] > distance[A] + C:
            distance[B] = distance[A] + C
            if i == N-1:
                print(-1)
                exit(0)

for dist in distance[1:]:
    if dist == sys.maxsize:
        print(-1)
    else:
        print(dist)