import sys

N, H = map(int, sys.stdin.readline().split())
height1 = [0 for _ in range(H)]
height2 = [0 for _ in range(H)]
minimum, count = N, 0

for i in range(N):
    target = int(sys.stdin.readline()) - 1
    if i % 2 == 0:
        height1[target] += 1
    else:
        height2[target] += 1

for j in range(H-2, -1, -1):
    height1[j] += height1[j + 1]
    height2[j] += height2[j + 1]

for k in range(H):
    if minimum > height1[k] + height2[H-k-1]:
        minimum, count = height1[k] + height2[H-k-1], 1
    elif minimum == height1[k] + height2[H-k-1]:
        count += 1

print(minimum, count)