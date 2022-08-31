class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(idx,path):
            if len(path) == k:
                res.append(path[:])
                return
            if idx > n:
                return
            for i in range(idx,n + 1):
                path.append(i)
                dfs(i + 1,path)
                path.pop()
        res = []
        dfs(1,[])
        return res