class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)

        for e in edges:
            graph[e[0]].append(vals[e[1]])
            graph[e[1]].append(vals[e[0]])

        for g in graph:
            graph[g].sort()
        ans = -inf
        for g in graph:
            temp = vals[g]
            numEdge = min(k,len(graph[g]))
            print(temp)
            for i in range(len(graph[g]) - numEdge, len(graph[g])):
                if graph[g][i] > 0:
                    temp += graph[g][i]
            ans = max(ans, temp)
        return max(max(vals), ans)
