class Solution:
    def reverse(self,l,r,arr):
        while l<r:
            arr[l],arr[r] = arr[r],arr[l]
            l+=1
            r-=1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.reverse(0,len(nums)-1,nums)
        k = k % len(nums)
        self.reverse(0,k-1,nums)
        self.reverse(k,len(nums)-1,nums)