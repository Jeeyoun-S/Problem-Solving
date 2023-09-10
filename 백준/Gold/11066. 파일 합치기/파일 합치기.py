import sys

T = int(sys.stdin.readline())

def dynamic(start, end):
    if dp[start][end] != -1:
        return dp[start][end]

    if start == end:
        return 0

    min_total = sys.maxsize
    summ = summ_files[end] - (summ_files[start-1] if start > 0 else 0)
    for i in range(start, end):
        total = dynamic(start, i) + dynamic(i+1, end) + summ
        if min_total > total:
            min_total = total
        dp[start][end] = min_total
    return min_total

for _ in range(T):
    K = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    summ_files = [files[0]]
    for i in range(1, K):
        summ_files.append((summ_files[i-1] + files[i]))

    dp = [[-1 for j in range(K+1)] for i in range(K+1)]
    result = dynamic(0, K-1)
    print(result)