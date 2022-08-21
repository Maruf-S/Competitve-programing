class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for fr,to,price in flights:
            adj[fr].append([to,price])
        
        stop = 0
        t = {}
        visit = set()
        q = [(0,0,src)]
        while q:
            pr,st,node = heapq.heappop(q)
            if node in t and t[node][1] <= st:
                continue
            if st - 1  > k:
                continue
            if node==dst:
                return pr
            t[node] = [pr,st]
            for to,price in adj[node]:
                heapq.heappush(q,(pr + price,st + 1,to))
        return -1