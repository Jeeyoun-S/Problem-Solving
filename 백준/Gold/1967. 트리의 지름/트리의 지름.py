import sys

sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())
nodes = [[] for _ in range(n)]
parents = set([i for i in range(n)])
result = 0

for _ in range(n-1):
    parent, child, cost = map(int, sys.stdin.readline().split())
    nodes[parent-1].append((child-1, cost))
    parents.remove(child-1)

def backtracking(point):

    if not nodes[point]:
        return 0

    results = []

    for _child, _cost in nodes[point]:
        results.append(_cost + backtracking(_child))

    results.sort()
    global result
    if len(results) >= 2:
        result = max(result, results[-1] + results[-2])
    elif len(results) == 1:
        result = max(result, results[-1])

    return results[-1]

parent = parents.pop()
backtracking(parent)

print(result)