class Solution:
    def maximumDetonation(self, arr: List[List[int]]) -> int:
        def canWake(node1,node2):
            x1,y1,r1 = node1
            x2,y2,r2 = node2
            dist = math.sqrt(((y2-y1) ** 2) + ((x2 - x1)**  2))
            return dist <= r1

        adj = [[] for _ in range(len(arr))]
        for i,j in enumerate(arr):
            for k,l in enumerate(arr):
                if i == k:
                    continue
                if canWake(j,l):
                    adj[i].append(k)

        def dfs(node,visit):
            visit[node] = True
            res = 1
            for nei in adj[node]:
                if not visit[nei]:
                    res += dfs(nei,visit)
            return res

        res = 1
        for baby in range(len(arr)):
            res = max(res,dfs(baby,[False] * len(arr)))
        return res