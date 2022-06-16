class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = []
        for i in range(len(nums)):
            if(nums[i] ==0):
                z.append(i)
        pc = 0
        for i in z:
            nums.pop(i-pc)
            pc+=1
        nums.extend([0]*(len(z)))
            