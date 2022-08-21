class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for (var1,var2),ans in zip(equations,values):
            adj[var1].append([var2,ans])
            adj[var2].append([var1,1/ans])
        
        def bfs(st,dst):
            if st not in adj or dst not in adj:
                return -1
            q = [(1,st)]
            visit = set([st])
            while q:
                w1, n1 = heapq.heappop(q)
                if n1 == dst:
                    return w1
                for n2,w2 in adj[n1]:
                    if n2 not in visit:
                        visit.add(n2)
                        heapq.heappush(q,[w2 * w1,n2])
            return -1
        res = []
        for q1,q2 in queries:
            res.append(bfs(q1,q2))
        return res