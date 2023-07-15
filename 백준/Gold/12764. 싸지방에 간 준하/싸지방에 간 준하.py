import sys
import heapq

N = int(sys.stdin.readline())
times = []
for _ in range(N):
    heapq.heappush(times, list(map(int, sys.stdin.readline().split())))
# print(times)
computer = 1
positions = [1]
empty = []
end_times = []
heapq.heappush(end_times, (heapq.heappop(times)[1], 0))
# print(end_times)

while times:
    start, end = heapq.heappop(times)

    while end_times and end_times[0][0] < start:
        time, number = heapq.heappop(end_times)
        heapq.heappush(empty, number)

    if not empty:
        heapq.heappush(end_times, (end, computer))
        positions.append(1)
        computer += 1
    else:
        number = heapq.heappop(empty)
        positions[number] += 1
        heapq.heappush(end_times, (end, number))

    # print(start, end, end_times, computer, positions)

print(computer)
print(*positions)