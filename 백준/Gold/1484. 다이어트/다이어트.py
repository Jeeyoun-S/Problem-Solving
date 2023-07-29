import sys

G = int(sys.stdin.readline())
result = []
A, B = 1, 1
while True:
    if (A**2 - B**2) > G:
        B += 1
    elif (A**2 - B**2) < G:
        A += 1
    else:
        result.append(A)
        A += 1
        B += 1
    if A == B:
        break

result = [-1] if len(result) == 0 else result
print(*result, sep="\n")