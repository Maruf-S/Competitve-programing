class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        k = 0
        for i in range(len(nums)-1):
            if(nums[i+1]<=nums[i]):
                need = (nums[i] - nums[i+1])+1
                nums[i+1]+=need
                k+=need
        return k