class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        i = 0
        ran = 0

        while i < len(nums):
            if nums[i] == 1:
                l = i
                while i + 1 < len(nums) and nums[i+1] == 1:
                    i += 1
                ran = max(ran,i-l+1)
                i += 1
                l = i
            else:
                i +=1
        return ran