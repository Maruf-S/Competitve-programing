class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)       # Height
        cols = len(grid[0])    # Width
        maxr = [max(row) for row in grid]     # As seen from left/right
        maxc = [max(col) for col in zip(*grid)]   # As seen from top/bottom
        tot = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] < maxr[i] and grid[i][j] < maxc[j]:
                    tot += min(maxr[i],maxc[j]) - grid[i][j]
        return tot