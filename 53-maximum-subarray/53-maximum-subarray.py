class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curmax = globalmax = nums[0]
        for i in nums[1:]:
            curmax = max(i,curmax + i)
            globalmax = max(globalmax,curmax)
        return globalmax