class Solution:
    def rob(self, nums: List[int]) -> int:
        maxi = 0
        d = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in d:
                return d[i]
            d[i] = nums[i] + max(dfs(i + 2),dfs(i + 3))
            return d[i]
        for i in range(len(nums)):
            maxi = max(dfs(i),maxi)
        return maxi