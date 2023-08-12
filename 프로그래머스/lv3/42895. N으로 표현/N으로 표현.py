import math

def solution(N, number):
    answer = 1
    results = [set([N])]
    if number == N:
        return answer

    while answer <= 8:
        new_set = set()
        
        for i in range(answer):
            for A in results[i]:
                for B in results[-i-1]:
                    new_set.add(A+B)
                    new_set.add(A*B)
                    new_set.add(A-B)
                    if B != 0:
                        new_set.add(A//B)
                        
        answer += 1                 
        new_set.add(int(str(N)*answer))    
        
        if number in new_set:
            return answer
        
        results.append(new_set)
    
    return -1