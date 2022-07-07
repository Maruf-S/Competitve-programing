class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l  = count= 0
        prod = 1
        for r in range(len(nums)):
            prod *= nums[r]
            while prod>=k and l <= r:
                prod /= nums[l]
                l+=1
            count+= (r-l) + 1
        return count