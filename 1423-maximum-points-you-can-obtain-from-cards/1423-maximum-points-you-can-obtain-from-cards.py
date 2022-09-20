class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        curr = 0
        l = 0
        minsum = float("inf")
        for r,val in enumerate(cp):
            curr += val
            if (r - l + 1) > len(cp) - k:
                curr -= cp[l]
                l += 1
            if (r - l + 1) == len(cp)-k:
                minsum = min(minsum,curr)
        return sum(cp) - minsum