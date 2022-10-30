class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[-1] = 1
        for i in range(len(dp) - 2, - 1, -1):
            res = dp[i + 1]
            if i + 2 < len(dp):
                res += dp[i + 2]
            dp[i] = res
        return dp[0]