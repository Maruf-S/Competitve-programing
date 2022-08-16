class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i : [] for i in range(n)}
        
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                d = abs(x1-x2) + abs(y1 - y2)
                adj[i].append([d,j])
                adj[j].append([d,i])
                
        h = [[0,0]]
        visit = set()
        tcost = 0
        while len(visit) < n:
            d,node = heapq.heappop(h)
            if node not in visit:
                visit.add(node)
                tcost += d
                for cost,neighbor in adj[node]:
                    if neighbor not in visit:
                        heapq.heappush(h,[cost,neighbor])
        return tcost