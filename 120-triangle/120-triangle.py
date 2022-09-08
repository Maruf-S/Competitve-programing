class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        dp = [[0] * len(j) for j in triangle]
        dp[-1] = triangle[-1]
        
        for i in range(rows-2,-1,-1):
            for j in range(len(dp[i])):
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j],dp[i + 1][j + 1])
        return dp[0][0]