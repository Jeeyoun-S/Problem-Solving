import sys

N = int(sys.stdin.readline())

def backtracking(num):
    global N
    if len(num) == N:
        print(num)
        exit(0)
    for i in '123':
        new_num = num + str(i)
        length = len(new_num)
        for idx in range(1, length // 2 + 1):
            if new_num[-idx:] == new_num[-(idx * 2):-idx]:
                break
        else:
            backtracking(new_num)
    return


backtracking('1')