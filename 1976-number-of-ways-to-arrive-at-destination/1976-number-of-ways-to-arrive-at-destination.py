class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v,t in roads:
            adj[u].append((t,v))
            adj[v].append((t,u))
        h = [(0,0)]
        arr = [float("inf")] * n
        while h:
            t,node = heappop(h)
            if t >= arr[node]:
                continue
            arr[node] = t
            for w,nei in adj[node]:
                heappush(h,(w + t,nei))
        mint = arr[-1]
        
        MOD = (10 ** 9 + 7)
        @cache
        def dp(i,total):
            if i == 0:
                return 1
            res = 0
            for wei, nei in adj[i]:
                if total + wei + arr[nei] != mint: continue        
                res = (res + dp(nei, total + wei)) % MOD
            return res
        return dp(n-1,0) 