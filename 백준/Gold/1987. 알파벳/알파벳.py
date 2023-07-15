import sys

R, C = map(int, sys.stdin.readline().split())
alphabets = [list(sys.stdin.readline().strip()) for _ in range(R)]
visited = [False for j in range(26)]
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
visited[ord(alphabets[0][0])-65] = True
result = 0


def backtracking(x, y, num):
    for dx, dy in delta:
        xx, yy = x+dx, y+dy
        if 0 <= xx < R and 0 <= yy < C:
            # print(xx, yy)
            # for v in visited:
            #     print(v)
            alphabet = ord(alphabets[xx][yy]) - 65
            if not visited[alphabet]:
                visited[alphabet] = True
                backtracking(xx, yy, num+1)
                visited[alphabet] = False


    global result
    result = max(result, num)


backtracking(0, 0, 1)
print(result)