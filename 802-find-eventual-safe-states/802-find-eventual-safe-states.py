class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []

        d = {}
        def dfs(node):
            if graph[node] == []:
                return True
            if node in d:
                return d[node]
            if node in visit:
                # Loop
                return False
            visit.add(node)
            for nei in graph[node]:
                if dfs(nei) == False:
                    d[node] = False
                    return False
            d[node] = True
            return True
        for i in range(len(graph)):
            visit = set()
            if dfs(i):
                res.append(i)
        return res