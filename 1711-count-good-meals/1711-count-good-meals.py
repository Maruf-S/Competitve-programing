import sys
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        count = 0
        d = Counter()
        for i,j in enumerate(nums):
            for k in range(22): 
                count += d[2**k - j]
            d[j]+=1
            
        return count % ((10**9) + 7)