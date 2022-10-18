class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        stack = []
        for i,j in enumerate(s):
            if j == "(":
                stack.append(i)
            else:
                if stack:
                    leftMost = stack.pop()
                    dp[i + 1] = dp[leftMost] + (i - leftMost + 1)
        return max(dp)