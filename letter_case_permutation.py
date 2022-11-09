class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        def helper(i,p):
            if i == len(s):
                res.append(p)
                return
            if s[i].isdigit():
                return helper(i + 1, p + s[i])
            helper(i + 1, p + s[i].upper())
            helper(i + 1, p + s[i].lower())
        res = []
        helper(0,"")
        return res
