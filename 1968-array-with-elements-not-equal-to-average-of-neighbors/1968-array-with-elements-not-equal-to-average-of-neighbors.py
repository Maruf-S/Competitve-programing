class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        inc = nums[1] > nums[0]
        for i in range(1,len(nums)-1):
            if (inc and nums[i+1] > nums[i]) or (not inc and nums[i+1] < nums[i]):
                nums[i+1],nums[i] = nums[i],nums[i+1]
            inc = not inc
        return nums