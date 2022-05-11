class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        j = 0
        for i in pushed:
            stack.append(i)
            while stack and popped[j] == stack[-1]:
                stack.pop()
                j+=1
        return stack==[]