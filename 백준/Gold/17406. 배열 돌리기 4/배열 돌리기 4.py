import sys
from itertools import permutations
from copy import deepcopy

# 배열 높이 N, 배열 너비 M, 회전 연산 개수 K
N, M, K = map(int, sys.stdin.readline().split())

# 회전 연산을 수행할 배열 A
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 회전 연산 리스트
calculate = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

# 우측 이동, 아래 이동, 좌측 이동, 위로 이동 시 움직여야 하는 dx, dy
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 결과값
result = sys.maxsize


# 회전 연산 함수 (가장 왼쪽 위 칸, 가장 오른쪽 아래 칸)
def turn(start_point, end_point):

    # 이전 위치의 값을 가장 왼쪽 위 칸으로 초기화
    before = B[start_point[0]][start_point[1]]
    
    # 시작 포인트는 가장 왼쪽 위 칸의 다음 칸
    now_point = (start_point[0], start_point[1]+1)

    # 이동 방향 : 0 우측 이동, 1 아래 이동, 2 좌측 이동, 3 위로 이동
    direction = 0
    
    # 움직여야 하는 범위 내인 경우 반복
    while start_point[0] <= now_point[0] <= end_point[0] and start_point[1] <= now_point[1] <= end_point[1]:

        after = B[now_point[0]][now_point[1]]   # 현재 값은 after에 넣고
        B[now_point[0]][now_point[1]] = before  # 이전 값이 before를 현재 위치에 넣는다.
        
        # 가장 왼쪽 위 칸으로 돌아왔다면 반복 중단
        if now_point == start_point:
            break
        
        # 꼭짓점에 도달했을 경우 방향 바꾸기
        if now_point[0] in (start_point[0], end_point[0]) and now_point[1] in (start_point[1], end_point[1]):
            direction = direction + 1
        
        # 다음 위치로 이동하고, before 값도 현재 값으로 바꿔준다.
        now_point = (now_point[0]+delta[direction][0], now_point[1]+delta[direction][1])
        before = after


# 연산 순서에 따라 반복하기
for perm in permutations(calculate, K):
    
    # A 배열 복사
    B = deepcopy(A)

    # 회전 연산을 반복하며 각 연산 수행하기
    for r, c, s in perm:
        start = (r-s-1, c-s-1)  # 가장 왼쪽 위 칸
        end = (r+s-1, c+s-1)    # 가장 오른쪽 아래 칸
        mid = (r-1, c-1)  # 중간 위치

        # 반복 시 가장 겉 테두리부터 회전시키며 점차 안으로 들어간다.
        # 네 방면 모두 안으로 한 칸씩 들어가야 하므로 number만큼 들어가는 것으로 계산
        number = 0

        # 중간 위치까지 반복
        while start[0] + number <= mid[0] and start[1] + number <= mid[1] and end[0] - number >= 0 and end[1] - number >= 0:
            # 회전 연산 수행
            turn((start[0]+number, start[1]+number), (end[0]-number, end[1]-number))
            # 다음 연산을 위해 number+1
            number += 1

    # 결과 구하기
    for bb in B:
        result = min(sum(bb), result)

print(result)