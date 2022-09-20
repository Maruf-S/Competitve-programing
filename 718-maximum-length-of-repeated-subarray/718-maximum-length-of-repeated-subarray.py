class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums2=''.join([chr(i) for i in nums2])
        mx=""
        ans=0
        for i in nums1:
            mx+=chr(i)
            if(mx in nums2):
                ans=max(ans,len(mx))
            else:
                mx=mx[1:]
        
        return ans