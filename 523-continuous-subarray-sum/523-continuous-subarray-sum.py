class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:-1}
        psum = 0
        for i,j in enumerate(nums):
            psum += j
            r =  psum % k
            if r not in d:
                d[r] = i
            elif i - d[r] >= 2:
                return True
        return False