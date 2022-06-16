class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        ran = 0
        for i, n in enumerate(nums):
            k -= (1 - n)
            if(k < 0):
                k += (1-nums[l])
                l += 1
            ran = max(ran, i-l+1)
        print(ran)
        return ran
