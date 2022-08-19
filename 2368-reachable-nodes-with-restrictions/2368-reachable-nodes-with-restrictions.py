class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        adj = {i:[] for i in range(n)}
        visited = set()
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        q = deque([0])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for nei in adj[node]:
                    if nei not in restricted:
                        q.append(nei)
        return len(visited)