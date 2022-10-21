class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[src] = 0
        for i in range(k + 1):
            tempDist = dist[:]
            for fr,to,price in flights:
                if dist[fr] + price < tempDist[to]:
                    tempDist[to] = dist[fr] + price
            dist = tempDist
        return -1 if dist[dst] == float("inf") else dist[dst]