import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
infos = sys.stdin.readline().split()
heap = []
for _ in range(M):
    u, v, d = map(int, sys.stdin.readline().split())
    if infos[u-1] == infos[v-1]:
        continue
    heapq.heappush(heap, (d, u-1, v-1))

parents = [i for i in range(N)]
def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

pick, total = 0, 0
while heap:
    cost, a, b = heapq.heappop(heap)
    pa, pb = find_parent(a), find_parent(b)
    if pa != pb:
        parents[pa] = pb
        total += cost
        pick += 1

        if pick >= N-1:
            break

if pick >= N-1:
    print(total)
else:
    print(-1)