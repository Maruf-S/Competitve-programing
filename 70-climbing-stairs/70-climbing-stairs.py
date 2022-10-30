class Solution:
    def climbStairs(self, n: int) -> int:
        first = 0
        second = 1
        for i in range(n):
            cur = first + second
            first = second
            second = cur
        return second