class UF():
    def __init__(self,n):
        self.rank = [1] * n
        self.par = [i for i in range(n)]
    
    def find(self,n):
        while self.par[n] != n:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    def union(self,n1,n2):
        par1 = self.find(n1)
        par2 = self.find(n2)
        
        if par1 == par2:
            return False
        if self.rank[par1] > self.rank[par2]:
            self.rank[par1] += self.rank[par2]
            self.par[par2] = par1
        else:
            self.rank[par2] += self.rank[par1]
            self.par[par1] = par2
        return True

            
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        uf = UF(rows * cols)
        dirn = [[1,0],[-1,0],[0,1],[0,-1]]
        def isBound(r,c):
            return 0 <= r < rows and 0 <= c < cols
        component = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    component += 1
                    curId = i * cols + j
                    for i1,j1 in dirn:
                        nr,nc = i1 + i, j1 + j
                        newId = nr * cols + nc
                        if isBound(nr,nc) and grid[nr][nc] == "1":
                            if uf.union(curId,newId):
                                component -= 1
        return component
            
# class UnionFind:
#     def __init__(self):
#         self.parent = {}
#         self.rank = {}
        
#     def union(self, x, y):
#         findX, findY = self.find(x), self.find(y)
#         if findX != findY:
#             self.parent[y] = x
        
#     def find(self, x):
#         if x not in self.parent:
#             self.parent[x] = x
#             self.rank[x] = 0
#             return x
#         p = self.parent[x]
#         while p!= self.parent[p]:
#             # path compression
#             self.parent[p] = self.parent[self.parent[p]]
#             p = self.parent[p]
#         return p
