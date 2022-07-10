class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = l = 0
        r = len(nums)-1
        while l<r:
            tsum = nums[l] + nums[r]
            if tsum == k:
                count +=1
                l+=1
                r-=1
            if tsum < k:
                 l+=1
            if tsum > k:
                r -=1
        return count