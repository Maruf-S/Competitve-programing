class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        
    def union(self, x, y):
        findX, findY = self.find(x), self.find(y)
        if findX != findY:
            if self.rank[findY] > self.rank[findX]:
                self.rank[findY] += 1
                self.parent[findX] = findY
            else:
                self.rank[findX] += 1
                self.parent[findY] = findX
        
    def find(self, x):
        # if x not in self.parent:
        #     self.parent[x] = x
        #     self.rank[x] = 0
        # if self.parent[x] == x:
        #     return x
        # return self.find(self.parent[x])
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x
        p = self.parent[x]
        while p!= self.parent[p]:
            p = self.parent[p]
        return p

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        users = {}
        uf = UnionFind()
        for i,(name,*emails) in enumerate(accounts):
            for email in emails:
                if email in users:
                    uf.union(i,users[email])
                users[email] = i
        ans = defaultdict(list)
        for user,par in users.items():
            ans[uf.find(par)].append(user)
        res = []
        for idx, users in ans.items():
            res.append([accounts[idx][0]] + sorted(users))
        return res            