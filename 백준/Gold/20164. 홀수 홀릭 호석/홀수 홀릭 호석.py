import sys

N = sys.stdin.readline().strip()
min_result, max_result = sys.maxsize, 0

def get_odd_cnt(num):
    count = 0
    for n in num:
        if int(n) % 2 == 1:
            count += 1
    return count

def backtracking(num, cnt):
    next_cnt = cnt + get_odd_cnt(num)
    if len(num) == 1:
        global min_result
        min_result = min(min_result, next_cnt)
        global max_result
        max_result = max(max_result, next_cnt)
        return
    elif len(num) == 2:
        backtracking(str(int(num[0]) + int(num[1])), next_cnt)
    else:
        length = len(num)
        for i in range(0, length-2):
            for j in range(i+1, length-1):
                one, two, three = int(num[0:i+1]), int(num[i+1:j+1]), int(num[j+1:length])
                backtracking(str(one + two + three), next_cnt)


backtracking(N, 0)
print(min_result, max_result)
