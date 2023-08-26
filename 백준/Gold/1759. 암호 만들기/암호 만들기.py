import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
alphabets = sys.stdin.readline().strip().split()
aeiou = "aeiou"
result = []
# print(alphabets)

for words in combinations(alphabets, L):
    A, B = 0, 0
    for word in words:
        if word in aeiou:
            A += 1
        else:
            B += 1
        if A >= 1 and B >= 2:
            words = sorted(list(words))
            result.append("".join(words))
            break

    # print(words)

result.sort()
print(*result, sep="\n")