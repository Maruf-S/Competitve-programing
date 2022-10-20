class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flights_to = defaultdict(list)
        for fr,to,price in flights:
            flights_to[fr].append((price,to))
        
        heap = [(0,src,0)]
        visited = set()
        while heap:
            cost,dest,stops = heappop(heap)
            if (dest, stops) in visited or stops > k + 1: 
                continue
            visited.add((dest, stops))
            if dest == dst:
                return cost
            for w_nei,nei in flights_to[dest]:
                heappush(heap,(cost + w_nei, nei,stops + 1))
        return -1