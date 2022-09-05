class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        maxArr = [float("-inf")] * len(nums)
        minArr = [float("inf")] * len(nums)
        
        prevMax = float("-inf")
        prevMin = float("inf")
        for i in range(len(nums)):
            prevMin = min(prevMin,nums[i])
            minArr[i] = prevMin
        for i in range(len(nums)-1,-1,-1):
            prevMax = max(prevMax,nums[i])
            maxArr[i] = prevMax
        for i in range(1,len(nums) - 1 ):
            if minArr[i] < nums[i] < maxArr[i]:
                return True
        return False