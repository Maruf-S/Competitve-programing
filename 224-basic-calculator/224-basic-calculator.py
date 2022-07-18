class Solution:
    def calculate(self, s):
        i = num = 0
        sign = 1
        res = 0
        stack = []
        while i < len(s):
            cur = s[i]
            if cur.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                num = int(s[start:i])
                continue
            elif cur in "-+":
                res += num * sign
                sign = -1 if cur == "-" else 1
                num = 0
            elif cur == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif cur == ")":
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
            i += 1
        return res + num *sign