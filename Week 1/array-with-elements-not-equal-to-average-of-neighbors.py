class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[inta
        """
        clear = False
        while(clear==False):
            clear = True
            for i in range(1,len(nums)-1):
                if(nums[i]==(nums[i-1]+nums[i+1])/2):
                    nums[i-1],nums[i] = nums[i],nums[i-1]
                    clear = False
        return (nums) 
        