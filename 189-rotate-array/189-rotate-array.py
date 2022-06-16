class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        res = [0]*n
        for i in range(n):
            if(i+k <= n-1):
                res[i+k] = nums[i]
            else:
                res[(i+k)%n] = nums[i]
        nums[:] = list(res)
            