class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        d = {"B":0,"W":0}
        l = 0
        res = float("inf")
        for i,j in enumerate(blocks):
            d[j] += 1
            while d["B"] + d["W"] >= k:
                    res = min(res,d["W"])
                    d[blocks[l]] -= 1
                    l += 1
        return res