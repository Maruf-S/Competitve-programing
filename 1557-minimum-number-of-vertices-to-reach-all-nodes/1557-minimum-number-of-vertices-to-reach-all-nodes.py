class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
        visited = set()
        res = set()
        def dfs(i):
            if i not in visited:
                visited.add(i)
                for nei in adj[i]:
                    if nei not in visited:
                        dfs(nei)
                    else:
                        res.discard(nei)
        for i in range(n):
            if i not in visited:
                dfs(i)
                res.add(i)
        return res