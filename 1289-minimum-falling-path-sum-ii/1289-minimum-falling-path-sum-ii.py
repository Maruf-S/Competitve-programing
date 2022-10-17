class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        @cache
        def dp(prev,r):
            if r == rows:
                return 0
            vals = map(lambda x: x[1], heapq.nsmallest(2, [(grid[r][i],i) for i in range(cols) if i!=prev]))
            return min(grid[r][v] + dp(v,r + 1) for v in vals)
        
        return dp(-1,0)