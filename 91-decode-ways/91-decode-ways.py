class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1
        dp = {}
        def dfs(i):
            if i == len(s):
                return 1
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            
            if i + 1 < len(s) and 10 <= int(s[i : i + 2]) <=26:
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)