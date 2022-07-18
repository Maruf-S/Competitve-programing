class Solution:
    def calculate(self, s):
        def update(num,sign):
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
        i, num, stack, sign = 0, 0, [], "+"
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = num*10 + int(c)
            elif c in "+-":
                update(num,sign)
                num = 0
                sign = c
            elif c == "(":
                res,j = self.calculate(s[i+1:])
                # update(res,sign)
                num = res
                i = i + j 
            elif c == ")":
                update(num,sign)
                return sum(stack), i + 1
            i+=1
        update(num,sign)
        return sum(stack)