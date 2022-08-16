class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for fr,to,price in flights:
            adj[fr].append([to,price])
        
        stop = 0
        t = {}
        visit = set()
        q = [(0,0,src)]
        if adj[src] == []:
            return -1
        while q:
            pr,st,node = heapq.heappop(q)
            # print(pr,st,node)
            if node == 3:
                print(pr,st,node)
                # print(st - 1 , " #")
            if node in t and t[node][1] <= st:
                continue
            if st - 1  > k:
                continue
            if node==dst:  # reach the destination # as priority_queue is a minHeap so this cost is the most minimum cost.
                return pr
            t[node] = [pr,st]
            for to,price in adj[node]:
                heapq.heappush(q,(pr + price,st + 1,to))
        print(adj)
        print(t)
        if dst not in t:
            return -1
        if t[dst][1] > k + 1:
            return -1
        return t[dst][0]
    # n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0