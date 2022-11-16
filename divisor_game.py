class Solution:
    def divisorGame(self, n: int) -> bool:
        @lru_cache(None)
        def dp(n, turn):
            if n == 0:
                return not turn
            if turn:
                return any(dp(n - x, False)
                           for x in range(1, n) if n % x == 0)
            else:
                return all(dp(n - x, True)
                           for x in range(1, n) if n % x == 0)
            
        return dp(n, True)
