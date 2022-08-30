class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(path, summ, idx):
            if len(path) > k or summ > n:
                return
            if summ == n and len(path) == k:
                res.append(path[:])
                return
            for i in range(idx,10):
                path.append(i)
                dfs(path, summ+i, i+1)
                path.pop()
        dfs([], 0, 1)
        return res