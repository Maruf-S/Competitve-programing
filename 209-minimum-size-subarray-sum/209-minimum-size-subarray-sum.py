class Solution:
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:
        n = len(nums) + 1
        mw = n
        cur = 0
        l = 0
        for i,j in enumerate(nums):
            cur += j
            if cur >= k:
                mw = min(mw,i-l+1)
            while cur - nums[l] >=k:
                cur-=nums[l]
                l += 1
                mw = min(mw,i-l+ 1)
        return mw if mw!=n else 0