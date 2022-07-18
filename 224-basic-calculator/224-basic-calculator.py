class Solution:
    def calculate(self, s):
        def calc(i):
            def update(num,sign):
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
            num, stack, sign = 0, [], "+"
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    num = num*10 + int(c)
                elif c in "+-":
                    update(num,sign)
                    num = 0
                    sign = c
                elif c == "(":
                    res,j = calc(i+1)
                    update(res,sign)
                    num = 0
                    i = j
                elif c == ")":
                    update(num,sign)
                    return sum(stack), i
                i+=1
            update(num,sign)
            return sum(stack)
        return calc(0)