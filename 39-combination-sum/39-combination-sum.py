class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(idx,path,total):
            if total == target:
                res.append(path.copy())
                return
            if idx == len(candidates) or total > target:
                return
            for i in range(idx,len(candidates)):
                path.append(candidates[i])
                dfs(i,path, total + candidates[i])
                path.pop()
        res = []
        dfs(0,[],0)
        return res