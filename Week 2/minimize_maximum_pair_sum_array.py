class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l = 0
        r= len(nums)-1
        mpa = 0
        while(l<r):
            mpa = max(mpa,nums[l]+nums[r])
            l+=1
            r-=1
        return mpa
        