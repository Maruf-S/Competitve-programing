class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s//2
        dp = [[False for i in range(target + 1)] for i in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
        for i in range(1,len(dp)):
            for j in range(len(dp[0])):
                notPick = dp[i - 1][j]
                pick = False
                if j - nums[i] >= 0:
                    pick = dp[i - 1][j - nums[i]]
                
                dp[i][j] = pick or notPick
                
        return dp[-1][-1]
    
    
    
