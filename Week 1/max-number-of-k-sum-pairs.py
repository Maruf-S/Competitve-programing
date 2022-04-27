class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l = 0
        r = len(nums)-1
        good_pairs = 0
        while(l<r):
            val = nums[l]+nums[r] 
            if(val==k):
                good_pairs+=1
                l+=1
                r-=1
            elif(val>k):
                r-=1
            else:
                l+=1
        return good_pairs