class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        grid = [[0] * len(colSum) for i in range(len(rowSum))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= grid[i][j]
                colSum[j] -= grid[i][j]
        return grid

