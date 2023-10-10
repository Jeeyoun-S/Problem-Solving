N = int(input())
people = list(map(int, input().split()))
B, C = map(int, input().split())
total = 0

for num in people:
    if num <= B:
        total += 1
        continue
    rest = num - B
    total += (rest // C) + (1 if rest % C > 0 else 0) + 1

print(total)