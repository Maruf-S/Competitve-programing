class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] > nums[i] :
                i += 1
                continue
            else:
                ops  += (nums[i] - nums[i + 1] + 1)
                nums[i + 1] += (nums[i] - nums[i + 1] + 1)
        return ops