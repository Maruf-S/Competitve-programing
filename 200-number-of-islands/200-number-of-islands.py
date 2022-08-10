class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        islands = 0
        def dfs(r,c):
            if not  r < ROW or r < 0:
                return
            if not c < COL or c < 0:
                return
            if grid[r][c] == "0" or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    islands += 1
        return islands

# [["1","1","1","1","0"]
#  ["1","1","0","1","0"]
#  ["1","1","0","0","0"]
#  ["0","0","0","0","0"]]
