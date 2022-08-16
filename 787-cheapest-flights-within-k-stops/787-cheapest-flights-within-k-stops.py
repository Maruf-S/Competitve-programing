class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         adj = defaultdict(list)
#         for fr,to,price in flights:
#             adj[fr].append([to,price])
        
#         stop = 0
#         t = {}
#         visit = set()
#         q = [(0,src,0)]
        
#         while q:
#             st,pr,dest = heapq.heappop(q)
#             t[dest] = [pr,st]
#             for to,price in adj[dest]:
#                 if to not in t:
#                     heapq.heappush(q,(st + 1,pr + price,to))
#                 else:
#                     if st  + 1 > k + 1:
#                         pass
#                     else:
#                         if pr + price < t[to][0]:
#                             heapq.heappush(q,(st + 1,pr + price,to))
                            
#         if dst not in t:
#             return -1
#         if t[dst][1] > k + 1:
#             return -1
#         return t[dst][0]
    def findCheapestPrice(self,n, flights, src, dst, K):
        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w
        pq = [(0, src, K+1)]
        vis = [0] * n
        while pq:
            w, x, k = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] >= k:
                continue
            vis[x] = k
            for y, dw in graph[x].items():
                heapq.heappush(pq, (w+dw, y, k-1))
        return -1