import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
checklist = [[0 for j in range(len(B)+1)] for i in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            checklist[i][j] = checklist[i-1][j-1] + 1
        else:
            checklist[i][j] = max(checklist[i-1][j], checklist[i][j-1])

print(checklist[len(A)][len(B)])