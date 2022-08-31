class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx,path,total):
            if total == target:
                res.append(path.copy())
                return
            if idx == len(candidates) or total > target:
                return
            for i in range(idx,len(candidates)):
                if i > idx and candidates[i -1] == candidates[i]:
                    continue
                path.append(candidates[i])
                dfs(i + 1,path, total + candidates[i])
                path.pop()
        res = []
        candidates.sort()
        dfs(0,[],0)
        return res    
