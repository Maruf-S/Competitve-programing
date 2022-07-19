class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_cur = nums[0]
        global_max = nums[0]
        for i in range(1,len(nums)):
            max_cur = max(nums[i], max_cur + nums[i])
            global_max = max(max_cur,global_max)
        return global_max