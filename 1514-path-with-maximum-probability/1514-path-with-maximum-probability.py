class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = {i:[] for i in range(n)}
        for (s,e),w in zip(edges,succProb):
            adj[s].append([-w,e])
            adj[e].append([-w,s])
        
        h = [[1,start]]
        t = [float('inf')] * n
        t[start] = 0
        visit = set([start])
        while h:
            w1,n1 = heapq.heappop(h)
            visit.add(n1)
            if n1 == end:
                return - w1
            for w2,n2 in adj[n1]:
                new_weight = - abs(w1 * w2) 
                if n2 not in visit:
                    t[n2] = new_weight
                    heapq.heappush(h,(new_weight,n2))
        return 0 