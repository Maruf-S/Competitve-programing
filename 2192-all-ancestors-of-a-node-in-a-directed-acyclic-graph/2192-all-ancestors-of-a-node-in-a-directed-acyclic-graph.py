class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = []
        adj = defaultdict(list)
        incoming = [0] * n
        
        for f,t in edges:
            adj[f].append(t)
            incoming[t] += 1
        
        q = deque([i for i in range(n) if incoming[i] == 0])
        res = [set() for i in range(n)]
        
        while q:
            node = q.popleft()
            for nei in adj[node]:
                res[nei].add(node)
                for i in res[node]:
                    res[nei].add(i)
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    q.append(nei)
        return map(lambda x : sorted(x),res)