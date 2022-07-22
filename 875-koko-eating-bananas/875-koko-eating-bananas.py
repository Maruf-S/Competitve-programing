class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)
        res = mx
        l = 1
        r = mx
        while l <= r:
            k = (l + r)//2
            totalTime = 0
            for i in piles:
                totalTime+= (-(-i//k))
            if totalTime <= h:
                res = k
            if totalTime > h:
                l = k + 1
            elif totalTime <= h:
                r = k - 1
        return res