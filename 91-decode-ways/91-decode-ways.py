class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i):
            if i in d:
                return d[i]
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i : i + 2]) <= 26:
                res += dfs(i + 2)
            d[i] = res
            return res
        d = {}
        return dfs(0)