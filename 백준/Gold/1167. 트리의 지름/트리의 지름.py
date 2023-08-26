import sys
import heapq

V = int(sys.stdin.readline())
edges = [[] for i in range(V)]

for _ in range(V):
    line = list(map(int, sys.stdin.readline().split()))
    start = line[0]-1
    for i in range(1, len(line)-1, 2):
        edges[start].append((line[i]-1, line[i+1]))

answer = 0

def find(i):
    result = [-1 for _ in range(V)]
    result[i] = 0

    heap = []
    heapq.heappush(heap, (0, i))

    while heap:
        cost, idx = heapq.heappop(heap)
        for ii, cc in edges[idx]:
            c = cost+cc
            if result[ii] > c or result[ii] < 0:
                result[ii] = c
                heapq.heappush(heap, (c, ii))

    global answer
    maximum = max(result)
    answer = max(answer, maximum)
    # print(result)
    return result.index(max(result))

next_idx = find(0)
find(next_idx)
print(answer)