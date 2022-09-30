class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], it: List[int]) -> int:
        adj = defaultdict(list)
        for d,s in enumerate(manager):
            if s == -1:
                continue
            adj[s].append((it[s],d))
        ttr = [float("inf")] * n
        
        h = [(0,headID)]
        
        while h:
            w,node = heappop(h)
            if ttr[node] < w:
                continue
            ttr[node] = w
            for w1,nei in adj[node]:
                heappush(h,(w + w1,nei))
        return max(ttr)