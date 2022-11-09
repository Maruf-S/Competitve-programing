class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)https://github.com/Maruf-S/Competitve-programing
        s = n*(n+1)//2
        r = s - sum(set(nums))
        dup = sum(nums) + r - s
        return [dup, r]
