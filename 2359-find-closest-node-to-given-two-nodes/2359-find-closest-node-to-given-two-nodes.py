class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = defaultdict(list)
        for f,t in enumerate(edges):
            if t == -1:
                continue
            adj[f].append(t)
        def dijstra(n,arr):
            q = deque([(0,n)])
            while q:
                w,node = q.popleft()
                if w >= arr[node]:
                    continue
                arr[node] = w
                for nei in adj[node]:
                    q.append((w + 1,nei))
        arr1 = [float("inf")] * len(edges)
        arr2 = [float("inf")] * len(edges)
        dijstra(node1,arr1)
        dijstra(node2,arr2)
        res = [-1,float("inf")]
        for i,(d1,d2) in enumerate(zip(arr1,arr2)):
            if max(d1,d2) < res[1]:
                res = [i,max(d1,d2)]
        return res[0]