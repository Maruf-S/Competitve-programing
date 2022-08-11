class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        q = deque([(0,k)])
        t = [0] + [float("inf")] * n
        for u,v,w in times:
            adj[u].append((w,v))
        while q:
            w1,n1 = q.popleft()
            if w1 < t[n1]:
                t[n1] = w1
                for w,v in adj[n1]:
                    q.append((w + w1,v))
        mx = max(t)
        return mx if mx < float("inf") else -1
                    