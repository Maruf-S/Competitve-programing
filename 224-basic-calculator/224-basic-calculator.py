class Solution:
    def calculate(self, s):
        num = res = 0
        sign = 1
        stack = []
        for ss in s:
            if ss.isdigit():
                num = num*10 + int(ss)
            elif ss in "+-":
                res += sign * num
                sign = -1 if ss == "-" else 1
                num = 0
            elif ss == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                num = 0
                sign = 1
            elif ss == ")":
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
                sign  = 1
        return res + num*sign