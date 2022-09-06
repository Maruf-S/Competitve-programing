class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for i in nums:
            if not dp:
                dp.append(i)
                continue
            j = bisect_left(dp,i)
            if j == len(dp):
                dp.append(i)
            else:
                dp[j] = i
        return len(dp)
            