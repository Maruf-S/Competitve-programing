class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        psum = 0
        res = 0
        l = 0
        nums.sort()
        for i,j in enumerate(nums):
            psum += j
            while (i - l + 1) * j - psum > k:
                psum -= nums[l]
                l += 1
            res = max(res,i-l + 1)
        return res