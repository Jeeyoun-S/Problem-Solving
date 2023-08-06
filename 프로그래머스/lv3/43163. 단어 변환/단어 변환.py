import sys
from collections import deque

def solution(begin, target, words):
    answer = sys.maxsize
    N = len(begin)
    W = len(words)
    
    queue = deque()
    queue.append((begin, 0))
    visited = [False for _ in range(W)]
    
    while queue:
        now, level = queue.popleft()
        
        if now == target:
            answer = min(answer, level)
            continue
        
        for ww in range(W):
            if visited[ww]:
                continue
            
            total = 0
            for i in range(N):
                if words[ww][i] != now[i]:
                    total += 1
            if total == 1:
                queue.append((words[ww], level+1))
                visited[ww] = True
        
    if answer == sys.maxsize:
        return 0
    return answer