class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i,j in enumerate(nums):
            if k-j in d:
                return [i,d[k-j]]
            else:
                d[j] = i