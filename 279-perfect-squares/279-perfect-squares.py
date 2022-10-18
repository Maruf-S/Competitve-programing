class Solution:
    # def numSquares(self, n: int) -> int:
    #     num  = [i**2 for i in range(1, int(n**0.5)+1)]
    #     @cache
    #     def helper(total):
    #         if total > n:
    #             return float("inf")
    #         if total == n:
    #             return 0
    #         return 1 + min(helper(total + i) for i in num if i <= n)
    #     return helper(0)
    
    def numSquares(self,n):
        dp = [0] + [float('inf')]*n
        for i in range(1, n+1):
            for j in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], 1+dp[i-j*j]) 
        return dp[n]