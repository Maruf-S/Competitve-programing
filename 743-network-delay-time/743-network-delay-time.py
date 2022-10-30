class Solution:
    def networkDelayTime(self, netTimes: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n + 1)
        heap = [(0,k)]
        adj = defaultdict(list)
        for src,dest,w in netTimes:
            adj[src].append((w,dest))
        
        while heap:
            w,node = heappop(heap)
            if w < dist[node]:
                dist[node] = w
                for wn,nei in adj[node]:
                    heappush(heap,(wn + w, nei))
        if float("inf") in dist[1:]:
            return -1
        return max(dist[1:])