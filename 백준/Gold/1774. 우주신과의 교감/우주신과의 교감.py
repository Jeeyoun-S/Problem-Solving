from heapq import heappop, heappush
import sys


def find(x):
    if home[x] < 0:
        return x

    home[x] = find(home[x])
    return home[x]


def union(a, b):
    a, b = find(a), find(b)
    home[b] = a


N, M = map(int, sys.stdin.readline().split())
home = [-1] * (N + 1)
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
my_heap = []
answer, cnt = 0, 0

for i in range(N):
    for j in range(i+1, N):
        weight = pow(pow(arr[i][0] - arr[j][0], 2) + pow(arr[i][1] - arr[j][1], 2), 0.5)
        heappush(my_heap, (weight, i+1, j+1))

# 이제 주어지는 좌표들은 연결된 좌표이므로 연결시켜주기
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    if find(x) != find(y):
        union(x, y)
        cnt += 1

for i in range(len(my_heap)):
	# 우선순위 큐인 힙에서 최소값 하나씩 뽑아
    w, a, b = heappop(my_heap)
	# 해당 좌표들인 a와 b가 연결X 일 경우,
    if find(a) != find(b):
    	# 연결시켜주고 가중치 저장
        union(a, b)
        answer += w
        cnt += 1
        
		# N개의 정점을 가진 그래프의 최소 간선은 N-1개
        if cnt == N-1:
            break

print(format(answer, ".2f"))