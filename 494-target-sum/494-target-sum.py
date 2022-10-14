class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def helper(i,total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            return helper(i + 1, total + nums[i]) + helper(i + 1, total - nums[i])
        return helper(0,0)