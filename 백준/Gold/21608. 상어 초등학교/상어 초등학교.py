import sys

N = int(sys.stdin.readline())
students = N**2
chairs = [[0 for j in range(N)] for i in range(N)]
likes = [[] for _ in range(students+1)]
total = [0 for _ in range(students+1)]
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))

for _ in range(students):
    me, a, b, c, d = map(int, sys.stdin.readline().split())
    likes[me] = (a, b, c, d)

    x, y, empty, like, who = N-1, N-1, -1, -1, []
    for i in range(N):
        for j in range(N):
            if chairs[i][j] > 0:
                continue

            new_empty, new_like, new_who = 0, 0, []
            for di, dj in delta:
                if 0 <= i+di < N and 0 <= j+dj < N:
                    if chairs[i+di][j+dj] == 0:
                        new_empty += 1
                    if chairs[i+di][j+dj] in (a, b, c, d):
                        new_like += 1
                    if chairs[i+di][j+dj] > 0:
                        new_who.append(chairs[i+di][j+dj])

            if like < new_like:
                x, y, empty, like, who = i, j, new_empty, new_like, new_who
            elif like == new_like:
                if empty < new_empty:
                    x, y, empty, like, who = i, j, new_empty, new_like, new_who
                elif empty == new_empty:
                    if x > i:
                        x, y, empty, like, who = i, j, new_empty, new_like, new_who
                    elif x == i:
                        if y > j:
                            x, y, empty, like, who = i, j, new_empty, new_like, new_who

    chairs[x][y] = me
    total[me] = like
    for w in who:
        if me in likes[w]:
            total[w] += 1
    # print(">>>>>>>>>>>")
    # print(x, y, me)
    # print(who)
    # print(chairs)
    # print(likes)
    # print(total)

# print(chairs)
result = sum([10**(t-1) if t >= 1 else 0 for t in total])
print(result)