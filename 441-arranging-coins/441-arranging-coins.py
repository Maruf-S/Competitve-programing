class Solution:
    def arrangeCoins(self, n: int) -> int:
        def arrange(n,k):
            if n-k<0:
                return k-1
            return arrange(n-k,k+1)
        return arrange(n,0)
