class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def dfs(i,path):
            if len(path) == k:
                if n == sum(path):
                    res.append(path[:])
                return
            if i > 9:
                return
            path.append(i)
            dfs(i + 1,path)
            path.pop()
            dfs(i + 1,path)
        dfs(1,[])
        return res
