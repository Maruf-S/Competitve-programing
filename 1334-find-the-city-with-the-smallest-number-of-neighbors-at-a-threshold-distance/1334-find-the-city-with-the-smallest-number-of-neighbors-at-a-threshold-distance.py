class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], k: int) -> int:
        adj = {i:[] for i in range(n)}
        for f,t,w in edges:
            adj[f].append([t,w])
            adj[t].append([f,w])
        def getNeighbors(city):
            minh = [(0,city)]
            t = {i:float("inf") for i in range(n)}
            t[city] = 0
            res = 0
            visit = set()
            while minh:
                w,node = heappop(minh)
                for nei,wei in adj[node]:
                        if wei + w < t[nei] and wei + w <= k:
                            visit.add(nei)
                            t[nei] = wei + w
                            heapq.heappush(minh,(w + wei,nei))
            return len(visit)
        return max([(getNeighbors(city), city) for city in range(n)], key=lambda x: (-x[0], x[1]))[-1]