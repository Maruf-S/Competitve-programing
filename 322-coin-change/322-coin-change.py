class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return float("inf")
            return min(1 + dp(remain - coin) for coin in coins)
        
        r = dp(amount)
        if r == float("inf"):
            return -1
        return r