class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows,cols = len(matrix),len(matrix[0])
        dp = [[float("inf") for _ in range(cols + 2)] for _ in range(rows)]
        for i in range(cols):
            dp[0][i + 1] = matrix[0][i]
        print(dp)
        for i in range(1,rows):
            for j in range(0,cols):
                dp[i][j + 1] = min(dp[i][j + 1],matrix[i][j] + min(dp[i - 1][j],dp[i - 1][j + 1],dp[i -1][j + 2]))
        # for i in dp:
        #     print(i)
        return min(dp[-1])