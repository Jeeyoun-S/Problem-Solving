import sys

def solution(gems):
    types = {gem: 0 for gem in gems}
    G = len(gems)
    N = len(types)
    # print(N)
    
    result = [0, G]
    start, end, cnt = 0, 0, 1
    types[gems[start]] += 1
    
    while True:
        if cnt == N:
            gap1, gap2 = result[1] - result[0], end - start
            if gap1 > gap2 or (result[0] > start and gap1 == gap2):
                result = [start, end]
            
            types[gems[start]] -= 1
            if types[gems[start]] == 0:
                cnt -= 1
            start += 1
        
        if end+1 >= G:
            break
        
        end += 1
        if types[gems[end]] == 0:
            cnt += 1
        types[gems[end]] += 1

        while G > start+1 and types[gems[start]] > 1:
            types[gems[start]] -= 1
            start += 1
            
        # print(result, start, end, cnt, types)
    
    return [result[0]+1, result[1]+1]