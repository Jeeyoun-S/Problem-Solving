import sys
import math
import heapq

# sys.stdin = open('input.txt')

n,m = map(int, sys.stdin.readline().split())
cnt = m

gph=[[] for  _ in range(n+2)]
prev = [ 0 for _ in range(n+2)]

def dijk(node):
  dist=[math.inf for _ in range(n+2)]
  edges=[]
  dist[node]=0
  heapq.heappush(edges, (dist[node], node))
  while edges:
    cost,pos = heapq.heappop(edges)
    if dist[pos]<cost:
      continue
    for p,c in gph[pos]:
      c+=cost
      if dist[p]>c:
        dist[p]=c
        prev[p] = pos
        heapq.heappush(edges, (c,p))
  return dist

while cnt:
  cnt-=1
  a,b,c = map(int, sys.stdin.readline().split())
  gph[a].append((b,c))
  gph[b].append((a,c))

# print(dijk(1))
dijk(1)
cnt=0
for iter in prev:
  if iter!=0:
    cnt+=1
print(cnt)

for idx, item in enumerate(prev):
  if item!=0:
    print(idx, prev[idx])