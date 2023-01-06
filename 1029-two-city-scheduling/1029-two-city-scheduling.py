class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x : x[0] - x[1])
        n = len(costs)//2
        @cache
        def dp(i,k):
            if i == len(costs):
                if k == 0:
                    return 0
                return inf
            return min(costs[i][0] + dp(i + 1, k - 1),costs[i][1] + dp(i + 1, k))
        return dp(0,n)