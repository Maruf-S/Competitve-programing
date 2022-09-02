class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        rob1,rob2 = 0,0
        for i in nums:
            temp = max(rob1 + i,rob2)
            rob1 = rob2
            rob2 = temp
        return max(rob1,rob2)