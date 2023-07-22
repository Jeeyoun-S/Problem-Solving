import heapq

def solution(n, costs):
    parent = [i for i in range(n+1)]
    heap = []
    
    for cost in costs:
        # print(cost)
        heapq.heappush(heap, [cost[2], cost[0], cost[1]])
    
    def find_parent(x):
        if x != parent[x]:
            parent[x] = find_parent(parent[x])
        return parent[x]
    
    # print(heap)
    # print(visited)
    pick, total = 0, 0
    while heap and pick < n:
        pay, A, B = heapq.heappop(heap)
        PA, PB = find_parent(A), find_parent(B)
        if PA != PB:
            parent[PA] = PB
        # print(pay, A, B, visited[A], visited[B])
        # if visited[A] and visited[B]:
            # continue
        # visited[A], visited[B] = True, True
        # print(B, visited[B])
        # visited[B] = True
            total += pay
            pick += 1
        # print(pick)
    
    # answer = 0
    return total