class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        rows,cols = len(land),len(land[0])
        def dfs(i,j):
            if i >=rows or i < 0 or j >= cols or j < 0 or land[i][j] == 0:
                return (float("-inf"),float("-inf"))
            land[i][j] = 0
            r1,c1 = dfs(i+1,j)
            r2,c2 = dfs(i, j + 1)
            return (max(r1,r2,i),max(c1,c2,j))
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1:
                    x,y = dfs(i,j)
                    res.append([i,j,x,y])
        return res