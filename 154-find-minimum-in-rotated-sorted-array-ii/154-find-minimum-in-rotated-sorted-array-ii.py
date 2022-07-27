class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        mini = float("inf")
        while l <= r:
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            if nums[l] < nums[r]:
                mini = min(mini,nums[l])
                break
            m =  l + (r - l)//2
            mini = min(mini,nums[m])
            # l portion
            if nums[l] <= nums[m]:
                l = m  + 1
            # R sorted portioion
            else:
                r = m - 1
        return mini