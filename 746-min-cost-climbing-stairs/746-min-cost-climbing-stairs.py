class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[-1],dp[-2] = cost[-1],cost[-2]
        for i in range(len(cost) - 3,-1,-1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        print(dp)
        return min(dp[0],dp[1])