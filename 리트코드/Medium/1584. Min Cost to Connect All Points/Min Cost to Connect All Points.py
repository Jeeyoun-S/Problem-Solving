import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        N = len(points)
        parents = [i for i in range(N)]

        def find_parent(x):
            if x != parents[x]:
                parents[x] = find_parent(parents[x])
            return parents[x]
        
        heap = []
        for i in range(N):
            for j in range(i+1, N):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(heap, (distance, i, j))

        pick, total = 0, 0
        while heap and pick < N:
            distance, i, j = heapq.heappop(heap)
            pi, pj = find_parent(i), find_parent(j)
            if pi != pj:
                parents[pi] = pj
                total += distance
                pick += 1
        
        return total
