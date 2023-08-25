from collections import deque

def solution(n, edge):
    
    nodes = [[] for _ in range(0, n)]
    
    for e in edge:
        nodes[e[0]-1].append(e[1]-1)
        nodes[e[1]-1].append(e[0]-1)
    
    visited = [False for _ in range(n)]
    visited[0] = True
    
    queue = deque()
    queue.append((0, 0))
    
    answer, maximum = 0, 0
    
    while queue:
        idx, cost = queue.popleft()
        print(idx, cost)
        for node in nodes[idx]:
            if visited[node]:
                continue
            visited[node] = True
            
            new_cost = cost+1
            if new_cost > maximum:
                answer, maximum = 1, new_cost
            elif new_cost == maximum:
                answer += 1
                
            queue.append((node, new_cost))
    
    return answer