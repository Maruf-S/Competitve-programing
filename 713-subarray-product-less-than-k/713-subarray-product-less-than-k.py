class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l  = count = 0
        p =  1
        for i,j in enumerate(nums):
            p *= j
            while l <= i and  p >= k:
                p/=nums[l]
                l += 1
            count += (i-l+1)
        return count