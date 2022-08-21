class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        for n1, n2, w in edges:
            adj[n1].append((n2, w))
            adj[n2].append((n1, w))
        
        min_city, min_reach = None, float('inf')
        for i in range(n):
            cur_reach = self.findReachByDjikstra(i, adj, distanceThreshold, n)
            if cur_reach <= min_reach:
                min_city = i
                min_reach = cur_reach
        return min_city
            
    def findReachByDjikstra(self, node, adj, distance, n):
        dest = [float('inf')] * n
        dest[node] = 0
        heap = [(0, node)]
        visited = set()
        while heap:
            w1, n1 = heappop(heap)
            visited.add(n)
            for n2, w2 in adj[n1]:
                new_weight = w1 + w2
                if new_weight <= dest[n2]:
                    dest[n2] = new_weight
                    heappush(heap, (new_weight, n2))
        reach = 0
        for i in dest:
            if i <= distance:
                reach += 1
        return reach