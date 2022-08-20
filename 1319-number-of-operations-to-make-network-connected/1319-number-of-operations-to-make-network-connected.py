class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def find(n):
            p = par[n]
            while p != par[p]:
                p = par[p]
            return p
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return True
        rank = [1] * n
        par = [i for i in range(n)]
        visit = set()
        extra = 0
        group = 0
        for i,j in connections:
            if union(i,j) == True:
                group += 1
            else:
                extra += 1
        extran = n - group
        return extran - 1 if extra >= extran - 1 else -1