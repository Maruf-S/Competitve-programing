class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(res,visited,subset):
            if len(subset) == len(nums):
                res.append(subset[:])
            for i in range(len(nums)):
                if i not in visited:
                    if i in visited or (i > 0 and nums[i-1] == nums[i] and not i-1 in visited):
                        continue
                    visited.add(i)
                    subset.append(nums[i])
                    backtracking(res,visited,subset)
                    subset.pop()
                    visited.remove(i)
        visited = set()
        res = []
        backtracking(res,visited,[])
        return res