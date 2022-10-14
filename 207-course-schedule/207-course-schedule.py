class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        res = []
        adj = defaultdict(list)
        outgoing = [0] * n
        for i,j in pre:
            adj[j].append(i)
            outgoing[i] += 1
            
        q = deque([i for i in range(n) if outgoing[i] == 0])
        
        while q:
            node  = q.popleft()
            for nei in adj[node]:
                outgoing[nei] -= 1
                if outgoing[nei] == 0:
                    q.append(nei)
        return sum(outgoing) == 0