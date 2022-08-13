class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = False
        if nums[0] <= nums[-1]:
            inc = True
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i] and not inc:
                return False
            elif inc and nums[i-1] > nums[i]:
                return False
        return True