class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        d = {}
        def dp(k):
            nonlocal res
            if k > n:
                return 0
            if k == n:
                return 1
            if k + 1 not in d:
                d[k + 1] = dp(k + 1)
            if k + 2 not in d:
                d[k + 2] = dp(k + 2)
            return d[k + 1] + d[k + 2]
        return dp(0)