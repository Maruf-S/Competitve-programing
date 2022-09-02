class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robHelp(nums):
            rob1,rob2 = 0,0
            for i in nums:
                temp = max(i + rob1,rob2)
                rob1 = rob2
                rob2 = temp
                
            return max(rob1,rob2)
        return max(robHelp(nums[1:]),robHelp(nums[:len(nums)-1]))