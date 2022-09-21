class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dp(i,l):
            if l < 0:
                return False
            if i == len(s):
                return l == 0
            if s[i] == "(":
                return dp(i + 1,l + 1)
            elif s[i] == ")":
                return dp(i + 1,l - 1)
            return dp(i + 1, l + 1) or dp(i + 1, l) or dp(i + 1,l-1)
        return dp(0,0)