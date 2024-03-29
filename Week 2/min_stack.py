class MinStack(object):

    def __init__(self):
        self.min_Stack = []
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if(self.min_Stack == []):
            self.min_Stack.append(val)
        else:
            self.min_Stack.append(min(val,self.min_Stack[-1]))
        self.stack.append(val)
    def pop(self):
        """
        :rtype: None
        """
        self.min_Stack.pop()
        return self.stack.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_Stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()