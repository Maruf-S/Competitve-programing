class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l = total = window = 0
        nums.sort()
        for r in range(len(nums)):
            total += nums[r]
            while (r-l+1) * nums[r] > total+k :
                total-=nums[l]
                l +=1
            window = max(window,r-l+1)
        return window