class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(n):
            n = keyval[n]
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
        rank = [1] * 26
        par = [i for i in range(26)]
        chars = [chr(i) for i in range(ord('a'),ord('z')+1)]
        keyval = {j:i for i,j in enumerate(chars)}
        for i,j,k,l in equations:
            if j == "=":
                union(i,l)
        for i,j,k,l in equations:
            if j == "!":
                if find(i) == find(l):
                    return False
        return True