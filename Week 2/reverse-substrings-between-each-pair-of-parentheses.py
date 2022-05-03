class Solution(object):
    def reverseParentheses(self, s):
        stack  = []
        for i in s:
            if(i == ")"):
                queue = []
                while stack[-1] != "(":
                    queue.append(stack.pop())
                stack.pop()
                while queue != []:
                    stack.append(queue.pop(0))
            else:
                stack.append(i)
        return ''.join(stack)

