import sys

N = sys.stdin.readline().strip()
M = sys.stdin.readline().strip()
dp = []
results = []

for i in range(len(N)):
    dp.append([0 for j in range(len(M))])
    results.append(["" for j in range(len(M))])

    for j in range(len(M)):
        if N[i] == M[j]:
            if j == 0 or i == 0:
                results[i][j] = N[i]
                dp[i][j] = 1
                continue
            elif dp[i-1][j] < dp[i-1][j-1] + 1:
                dp[i][j] = dp[i-1][j-1] + 1
                results[i][j] = results[i-1][j-1] + N[i]

        if i > 0 and dp[i-1][j] > dp[i][j]:
            dp[i][j] = dp[i-1][j]
            results[i][j] = results[i-1][j]
        if j > 0 and dp[i][j-1] > dp[i][j]:
            dp[i][j] = dp[i][j-1]
            results[i][j] = results[i][j-1]

# print(*dp, sep="\n")
# print(*results, sep="\n")
print(dp[-1][-1])
if dp[-1][-1] > 0:
    print(results[-1][-1])