class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        
    def union(self, x, y):
        findX, findY = self.find(x), self.find(y)
        if findX != findY:
            self.parent[y] = x
        
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x
        p = self.parent[x]
        while p!= self.parent[p]:
            # path compression
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        uf = UnionFind()
        for i,j in edges:
            uf.union(i,j)
        res = []
        for i in range(n):
            if uf.parent[i] == i:
                res.append(i)
        return res