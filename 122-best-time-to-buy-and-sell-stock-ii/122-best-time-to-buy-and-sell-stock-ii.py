class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = {}
        def dfs(i,buying):
            if i >= len(prices):
                return 0
            if (i,buying) in d:
                return d[(i,buying)]
            if buying:
                sell = dfs(i + 1,False)
                d[(i,buying)] =  max(sell - prices[i],dfs(i + 1,True))
            else:
                d[(i,buying)] =  max(prices[i] + dfs(i + 1,True),dfs(i + 1,False))
            return d[(i,buying)]
        return dfs(0,True)
    
    
    
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         d = {}
#         def dp(i,flag):
#             if i == len(prices):
#                 return 0
#             if (i,flag) in d:
#                 return d[(i,flag)]
#             if flag: ## this means sell
#                 d[(i,flag)] = max(dp(i+1,not flag) + prices[i],dp(i+1,flag))
#             else:  ## this means buy
#                 d[(i,flag)] = max(dp(i+1,not flag) - prices[i],dp(i+1,flag))
#             return d[(i,flag)]
#         return dp(0,False)