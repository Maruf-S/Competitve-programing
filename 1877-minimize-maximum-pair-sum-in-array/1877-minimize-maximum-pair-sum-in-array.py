class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(list((nums[i] + nums[len(nums) - i - 1]) for i in range(len(nums))))