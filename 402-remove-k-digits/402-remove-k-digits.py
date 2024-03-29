class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in num:
            while k and stack and stack[-1]>i:
                k-=1
                stack.pop()
            stack.append(i)
        stack = stack[:len(stack)-k]
        res = "".join(stack)
        return str(int(res)) if res else "0"