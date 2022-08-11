class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj,visited = defaultdict(list),set()
        q = [(0,k)]
        t = {}
        for u,v,w in times:
            adj[u].append((w,v))
        while q:
            w1,n1 = heapq.heappop(q)
            if n1 not in visited:
                t[n1] = w1
                visited.add(n1)
                for w,v in adj[n1]:
                    heapq.heappush(q,(w + w1,v))
        return max(t.values()) if len(visited) == n else -1
                    