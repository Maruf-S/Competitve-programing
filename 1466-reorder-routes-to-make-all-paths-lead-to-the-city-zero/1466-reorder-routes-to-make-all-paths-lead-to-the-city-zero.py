class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connset = set(tuple(c) for c in connections)
        adj = defaultdict(list)
        for s,d in connections:
            adj[s].append(d)
            adj[d].append(s)
        visited = set([0])
        q = deque([0])
        ans = 0
        # print(adj)
        while q:
            node = q.popleft()
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    if (node,nei) in connset:
                        # print((node,nei))
                        ans += 1
                    visited.add(nei)
                    q.append(nei)
        return ans