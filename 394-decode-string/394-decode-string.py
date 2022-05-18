class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if(i!="]"):
                stack.append(i)
            else:
                m = ""
                while stack[-1] != "[":
                    m = stack.pop()+m
                stack.pop()
                n = ""
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                stack.append(m*int(n))
        return "".join(stack)