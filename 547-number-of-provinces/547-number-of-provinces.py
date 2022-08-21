class UnionFind():
    def __init__(self):
        self.par = {}
        self.rank = {}
    def find(self,n):
        if n not in self.par:
            self.par[n] = n
            self.rank[n] = 0
            return n
        p = self.par[n]
        while p != self.par[p]:
            p = self.par[p]
        return p
    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.rank[p1] += self.rank[p2]
                self.par[p2] = p1
            else:
                self.rank[p2] += self.rank[p1]
                self.par[p1] = p2
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        s = len(M)
        uf = UnionFind()
        for i in range(s):
            for j in range(s):
                if M[i][j] == 1:
                    uf.union(i,j)
        provinces = set(uf.find(i) for i in range(s))
        return len(provinces)