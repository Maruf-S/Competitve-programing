class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            if i == 0: dp[0][i] = grid[0][i]
            else: dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(n):
            if i == 0: dp[i][0] = grid[i][0]
            else: dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]