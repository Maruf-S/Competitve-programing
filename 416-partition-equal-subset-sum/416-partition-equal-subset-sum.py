class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums)//2
        
        @cache
        def doSolve(i,total):
            if i == len(nums):
                return False
            if total + nums[i] == target:
                return True
            return doSolve(i + 1, total + nums[i]) or doSolve(i + 1, total)
        return doSolve(0,0)