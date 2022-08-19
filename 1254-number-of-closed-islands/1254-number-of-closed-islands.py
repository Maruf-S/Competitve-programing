class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        dirn = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs1(r,c):
            if r == rows or  r < 0 or c == cols or c < 0 or grid[r][c] != 0:
                return
            grid[r][c] = -1
            
            for x,y in dirn:
                dfs1(r + x, y + c)
        
        for i in [0,rows-1]:
            for j in range(cols):
                if grid[i][j] == 0:
                    dfs1(i,j)
        for i in range(rows):
            for j in [0,cols- 1]:
                if grid[i][j] == 0:
                    dfs1(i,j)
        visit = set()
        
        def dfs(r,c):
            if r == rows or  r < 0 or c == cols or c < 0 or grid[r][c] == -1:
                return False
            if grid[r][c] == 1 or (r,c) in visit :
                return True
            visit.add((r,c))
            res = True
            for x,y in dirn:
                if dfs(r + x, y + c) == False:
                    res = False
            return res
        count = 0
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visit and grid[i][j] == 0:
                    if dfs(i,j):
                        count += 1
        return count