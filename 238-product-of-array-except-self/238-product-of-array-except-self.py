class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        pre = 1
        for i in range(len(nums)):
            output[i] = pre
            pre = nums[i] * pre
            
        pos = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] = output[i]*pos
            pos*= nums[i]
        return output