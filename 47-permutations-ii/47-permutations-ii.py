class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            for i in range(len(nums)):
                if i in visited or (i > 0 and nums[i-1] == nums[i] and i-1 not in visited):
                    continue
                visited.add(i)
                dfs(path + [nums[i]])
                visited.remove(i)
        res,visited = [],set()
        nums.sort()
        dfs([])
        return res