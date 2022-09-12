class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = {}
        
        def dfs(i,k,buying):
            if (i,k,buying) in d:
                return d[(i,k,buying)]
            if i >= len(prices) or k == 0:
                return 0
            if buying:
                d[(i,k,buying)] = max(dfs(i + 1, k - 1,False) - prices[i],dfs(i + 1,k,True))
            else:
                d[(i,k,buying)]  = max(prices[i] + dfs(i + 1,k-1,True),dfs(i + 1,k,False))
            return d[(i,k,buying)]
        return dfs(0,4,True)