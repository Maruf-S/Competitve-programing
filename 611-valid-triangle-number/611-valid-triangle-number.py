class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            r = i - 1
            l = 0
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    result += (r - l)
                    r -= 1
                else:
                    l += 1
        return result
#         [2, 2, 3, 4]
#          l     r  i
# #         for i in reversed(range(len(nums))):
#             left = 0
#             right = i - 1
#             while left < right:
#                 if nums[left] + nums[right] > nums[i]:
#                     result += (right - left)
#                     right -= 1
#                 else:
#                     left += 1
        
#         return result