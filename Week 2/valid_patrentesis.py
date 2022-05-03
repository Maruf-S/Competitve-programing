class Solution(object):
    def isValid(self, s):
        stack = []
        close_to_open = {")":"(","]":"[","}":"{"}
        for i in s:
            if i in close_to_open and len(stack)>0 and stack[-1] == close_to_open[i]:
                stack.pop()
            else:
                stack.append(i)
        return stack == []