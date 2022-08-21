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
            while minh:
                w,node = heappop(minh)
                for nei,wei in adj[node]:
                        if wei + w < t[nei] :
                            t[nei] = wei + w
                            heapq.heappush(minh,(w + wei,nei))
            res = -1
            for i in t.values():
                if i <= k:
                    res += 1
            return res
        return max([(getNeighbors(city), city) for city in range(n)], key=lambda x: (-x[0], x[1]))[-1]
    # def findReachByDjikstra(self, node, adj, distance, n):
    #     dest = [float('inf')] * n
    #     dest[node] = 0
    #     heap = [(0, node)]
    #     visited = set()
    #     while heap:
    #         w1, n1 = heappop(heap)
    #         visited.add(n)
    #         for n2, w2 in adj[n1]:
    #             if n2 not in visited:
    #                 new_weight = w1 + w2
    #                 if new_weight <= dest[n2]:
    #                     dest[n2] = new_weight
    #                     heappush(heap, (new_weight, n2))
    #     reach = 0
    #     for i in dest:
    #         if i <= distance:
    #             reach += 1
    #     return reach