class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        cache = {}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i == ROWS or j == COLS:
                return 0
            if grid[i][j] == 1:
                return 0
            if i==ROWS-1 and j== COLS-1:
                return 1
            cache[(i,j)] = dfs(i + 1,j) + dfs(i,j+1)
            return cache[(i,j)]
        return dfs(0,0)