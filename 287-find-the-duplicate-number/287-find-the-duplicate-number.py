class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 1
        r = len(nums) - 2
        while l <= r:
            m = (l+r)//2
            c = 0
            for i in nums:
                if i <= m:
                    c += 1
            if c > m:
                r = m - 1
            else:
                l = m + 1
        return l
                
#         low = 1
#         high = len(nums)-1
        
#         while low < high:
#             mid = low+(high-low)/2
#             count = 0
#             for i in nums:
#                 if i <= mid:
#                     count+=1
#             if count <= mid:
#                 low = mid+1
#             else:
#                 high = mid
#         return low