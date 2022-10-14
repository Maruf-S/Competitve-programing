class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        incoming = [0] * n
        adj = defaultdict(list)
        for i,j in pre:
            adj[j].append(i)
            incoming[i] += 1
        
        q = deque([i for i in range(n) if incoming[i] == 0])
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    q.append(nei)
        return res if len(res) == n else []