class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = float("inf")
        for i in range(1,7):
            missa,missb = 0,0
            for it,(top,bottom) in enumerate(zip(tops,bottoms)):
                if top != i and bottom!=i:
                    break
                missa += not top == i
                missb += not bottom == i
                if it == len(bottoms) - 1:
                    ans = min(missa,missb)
        return -1 if ans == float("inf") else ans