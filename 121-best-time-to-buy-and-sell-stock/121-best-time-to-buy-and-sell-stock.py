class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minp = float("inf")
        for i in prices:
            minp = min(minp,i)
            maxp = max(i-minp,maxp)
        return maxp