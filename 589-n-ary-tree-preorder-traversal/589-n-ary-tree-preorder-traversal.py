class Solution(object):
    def preorder(self, root):
        if root is None:
            return []
        
        stack = [root]
        output = []
        while stack:
            temp = stack.pop()
            output.append(temp.val)
            stack.extend(temp.children[::-1])
        return output
        