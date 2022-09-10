class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        d = {}
        def dfs(i,buy):
            if i >= len(prices):
                return 0
            if (i,buy) in d:
                return d[(i,buy)]
            if buy:
                d[(i,buy)] =  max(dfs(i + 1,False) - prices[i],dfs(i + 1,True))
            else:
                # SELL
                d[(i,buy)] =  max(dfs(i + 1,True) + prices[i] - fee, dfs(i + 1, False))
            return d[(i,buy)]
        return dfs(0,True)