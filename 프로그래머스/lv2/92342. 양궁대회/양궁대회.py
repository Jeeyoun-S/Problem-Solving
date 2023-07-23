def solution(n, info):
    
    result, maximum = [-1], 0
    
    def backtracking(results, i, pick):
        # print(i, pick, results)
        if i == 11:
            nonlocal result
            nonlocal maximum
            
            if pick < n:
                results[10] += n - pick
            
            apeach, lion = 0, 0
            for j in range(11):
                if info[j] < results[j]:
                    lion += 10 - j
                elif info[j] > 0:
                    apeach += 10 - j
            
            if lion > apeach:
                if result[0] < 0 or maximum < lion - apeach:
                    result = results[:]
                    maximum = lion - apeach
                elif maximum == lion - apeach:
                    start = 0
                    for k in range(10, -1, -1):
                        if start == 0:
                            if results[k] > result[k]:
                                start += 1
                            elif results[k] < result[k]:
                                break
                        result[k] = results[k]
            if pick < n:
                results[10] -= n - pick
            return
        
        arrow = info[i] + 1
        if arrow + pick <= n:
            results[i] = arrow
            backtracking(results, i+1, pick + arrow)
            results[i] = 0
        backtracking(results, i+1, pick)
    
    backtracking([0 for i in range(11)], 0, 0)
    
    return result