import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
roads = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M+1)]

def find_parents(x):
    if x != parents[x]:
        parents[x] = find_parents(parents[x])
    return parents[x]

def mst():
    peak, total = 0, 0
    while heap:
        C, A, B = heapq.heappop(heap)
        # print(C, A, B)
        PA, PB = find_parents(A), find_parents(B)
        if PA != PB:
            parents[PA] = PB
            if C == 0:
                total += 1
            peak += 1
        if peak >= N:
            break
    return total

heap, parents = [], [i for i in range(N+1)]
for A, B, C in roads:
    heapq.heappush(heap, (-C, A, B))
# print(heap)
min_total = mst()

heap, parents = [], [i for i in range(N+1)]
for A, B, C in roads:
    heapq.heappush(heap, (C, A, B))
# print(heap)
max_total = mst()

print(max_total**2 - min_total**2)