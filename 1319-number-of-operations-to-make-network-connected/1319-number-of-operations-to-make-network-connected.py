class UnionFind():
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    def find(self,x):
        p = self.parent[x]
        while p!= self.parent[p]:
            # path compression
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2
        return True
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(n)
        redundant, wires = 0, n-1
        
        for start, end in connections:
            if uf.union(start, end):
                wires -= 1
            else:
                redundant += 1

        return wires if wires <= redundant else -1