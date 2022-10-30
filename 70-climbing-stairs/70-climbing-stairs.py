class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def helper(c):
            if c > n:
                return 0
            if c == n:
                return 1
            return helper(c + 1) + helper(c + 2)
        return helper(0)