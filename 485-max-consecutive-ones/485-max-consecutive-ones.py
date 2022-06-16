class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        i = 0
        ran = 0

        while i < len(nums):
            if nums[i] == 1:
                l = i
                while i < len(nums) and nums[i] == 1:
                    i += 1
                ran = max(ran,i-l)
                l = i
            else:
                i +=1
        return ran