class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        tsum = sum(nums)
        res = []
        after = 0
        for i in nums[::-1]:
            tsum -= i
            after += i
            res.append(i)
            if after > tsum:
                return res