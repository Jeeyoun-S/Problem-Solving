from itertools import combinations

def solution(n, weak, dist):
    weak_len, friends_num = len(weak), len(dist)
    distance = []
    
    for idx in range(weak_len):
        if idx == (weak_len-1):
            distance.append(n - weak[idx] + weak[0] - 0)
        else:
            distance.append(weak[idx+1] - weak[idx])

    dist.sort(reverse=True)
    divide_point = [False for _ in range(weak_len)]
    
    for i in range(1, friends_num+1):
        for checklist in combinations(range(weak_len), i):
            
            for check in checklist:
                divide_point[check] = True
            
            divide_distance = []
            nexts = checklist[0]

            while True:
                total = 0
                after = (nexts + 1) % weak_len

                while not divide_point[after]:
                    total += distance[after]
                    after = (after + 1) % weak_len

                divide_distance.append(total)
                if after == checklist[0]:
                    break
                nexts = after
            divide_distance.sort(reverse=True)
            
            for j in range(i):
                if divide_distance[j] > dist[j]:
                    break
            else:
                return i

            for check in checklist:
                divide_point[check] = False

    return -1