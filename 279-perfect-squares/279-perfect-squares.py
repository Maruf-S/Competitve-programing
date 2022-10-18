class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        num  = [i**2 for i in range(1, int(n**0.5)+1)]
        @cache
        def helper(total):
            if total > n:
                return float("inf")
            if total == n:
                return 0
            return 1 + min(helper(total + i) for i in num if i <= n)
        return helper(0)