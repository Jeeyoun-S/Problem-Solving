import sys

N = int(sys.stdin.readline())
features = list(map(int, sys.stdin.readline().split()))
features.sort()
minimum, results = sys.maxsize, []

for i in range(N):
    start, end = 0, N-1
    if start == i:
        start += 1
    if end == i:
        end -= 1

    while start < end:
        total = features[start] + features[end] + features[i]
        if abs(total) < minimum:
            minimum = abs(total)
            results = [features[start], features[end], features[i]]

        if total < 0:
            start += 1
            if start == i:
                start += 1
        elif total > 0:
            end -= 1
            if end == i:
                end -= 1
        else:
            break

results.sort()
print(*results)