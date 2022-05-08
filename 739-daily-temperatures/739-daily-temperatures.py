class Solution(object):
    def dailyTemperatures(self,temps):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0]*len(temps)
        # Monotonically decreasing
        stack = []
        for i, t in enumerate(temps):
            if stack and stack[-1][1] < t:
                while(stack and stack[-1][1]<t):
                    ele = stack.pop()
                    ans[ele[0]] = i-ele[0]
            stack.append([i, t])
        return ans