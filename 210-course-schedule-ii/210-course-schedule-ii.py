class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i,j in pre:
            adj[i].append(j)
        res = []
        visited = set()
        visiting = set()
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            res.append(node)
            visited.add(node)
            visiting.remove(node)
            return True
        
        
        
        
        
        for i in range(n):
            if not dfs(i):
                return []
        return res