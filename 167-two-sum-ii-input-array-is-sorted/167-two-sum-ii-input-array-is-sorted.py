class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            op = nums[r] + nums[l]
            if op > k:
                r -=1
            if op < k:
                l += 1
            if op == k:
                return [l + 1 , r + 1]