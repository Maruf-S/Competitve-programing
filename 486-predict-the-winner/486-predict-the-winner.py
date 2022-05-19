class Solution(object):
    def PredictTheWinner(self, nums):
        n = len(nums)
        
        def dfs(i, j):
            if i == j:
                return nums[i]

            pick_left = nums[i] - dfs(i+1, j)
            pick_right = nums[j] - dfs(i, j-1)
            
            return max(pick_left, pick_right)
        
        return dfs(0, n-1) >= 0
        