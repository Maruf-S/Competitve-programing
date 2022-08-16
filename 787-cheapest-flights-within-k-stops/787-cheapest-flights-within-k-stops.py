class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf") for i in range(n)]
        prices[src] = 0
        for i in range(k + 1):
            tempPrices = prices[:]
            for fro,to,price in flights:
                if fro == float("inf"):
                    continue
                temp = prices[fro] + price
                if temp < tempPrices[to]:
                    tempPrices[to] = temp
            prices = tempPrices
        return -1 if prices[dst] == float("inf") else prices[dst]