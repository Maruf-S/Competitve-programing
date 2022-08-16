class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows,cols = len(grid2),len(grid2[0])
        
        visit = set()
        islands = 0
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visit or grid2[r][c] != 1:
                return True
            if grid1[r][c] != 1:
                return False
            visit.add((r,c))
            direction =  [[1,0],[-1,0],[0,-1],[0,1]]
            out = True
            for i1,j1 in direction:
                if dfs(r+ i1,c + j1) == False:
                    out = False
            return out
            
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and (i,j) not in visit and dfs(i,j) == True:
                    islands += 1
        return islands