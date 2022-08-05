class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l <= r:
            print(l,r)
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -=1
            m = (l+r)//2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m-1
            else:
                left = m
                right = m
                while left - 1 >= 0 and nums[left] == nums[left - 1]:
                    left -= 1
                while right + 1 < len(nums) and nums[right] == nums[right + 1]:
                    right += 1
                return [left,right]
                    
        return [-1,-1]