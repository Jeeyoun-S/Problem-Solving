import sys
import heapq

T = int(sys.stdin.readline())
for tc in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())

    roads = [[] for _ in range(n+1)]
    for i in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        roads[a].append((d, b))
        roads[b].append((d, a))

    destinations = [int(sys.stdin.readline()) for j in range(t)]
    nodes = []
    heapq.heappush(nodes, (0, s))
    visited = [float("inf") for _ in range(n+1)]

    while nodes:
        cost, a = heapq.heappop(nodes)
        # print(cost, a, visited, visited[a])
        if cost > visited[a]:
            continue
        elif cost < visited[a]:
            visited[a] = cost
            for link in roads[a]:
                new_cost = cost + link[0] - 0.1 if (link[1] == g and a == h) or (link[1] == h and a == g) else cost + link[0]
                heapq.heappush(nodes, (new_cost, link[1]))

    result = []
    # print(visited)
    # print(visited[3] // 1, visited[3] - 1)
    for destination in destinations:
        if visited[destination] - (visited[destination] // 1) > 0:
            result.append(destination)
    result.sort()
    print(*result)