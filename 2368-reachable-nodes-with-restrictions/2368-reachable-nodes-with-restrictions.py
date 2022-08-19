class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        adj = {i:[] for i in range(n)}
        visited = set([0])
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        q = deque([0])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                for nei in adj[node]:
                    if nei not in restricted and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
        return len(visited)