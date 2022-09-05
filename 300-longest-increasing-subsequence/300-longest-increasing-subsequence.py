class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = 1
        for i in range(len(nums) - 2,-1,-1):
            res = 0
            for j in range(i + 1,len(dp)):
                if nums[i] < nums[j]:
                    res = max(res,dp[j])
            dp[i] = res + 1
        return max(dp)
                