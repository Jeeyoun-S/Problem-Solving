import sys

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
maximum = max(abs(r1), abs(c1), abs(r2), abs(c2))
N = (maximum*2)+1
results = [[0 for j in range(c1+maximum, c2+maximum+1)] for i in range(r1+maximum, r2+maximum+1)]
delta = (0, -1)
max_len = 0
start, end, number, length = N-1, N-1, N*N, 0
while number >= 1:

    if r1 <= start - maximum <= r2 and c1 <= end - maximum <= c2:
        results[-(maximum+r1)+start][-(maximum+c1)+end] = number
        max_len = max(max_len, len(str(number)))

    number -= 1

    if start == N-1-length and end == length:
        # print(1)
        delta = (-1, 0)
    elif start == length and end == length:
        # print(2)
        delta = (0, 1)
    elif start == length and end == N-1-length:
        # print(3)
        delta = (1, 0)
    elif start == N-1-length-1 and end == N-1-length:
        # print(4)
        delta = (0, -1)
        length += 1

    start += delta[0]
    end += delta[1]

for result in results:
    row = ''
    for i, r in enumerate(result):
        if i > 0:
            row += " "
        row += ((max_len - len(str(r))) * ' ') + str(r)
    print(row)