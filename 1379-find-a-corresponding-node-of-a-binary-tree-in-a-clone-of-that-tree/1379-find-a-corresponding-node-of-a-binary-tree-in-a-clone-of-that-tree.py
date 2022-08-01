# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        steps = []
        def dfs(original):
            if not original:
                return None
            l =  dfs(original.left)
            if original.val == target.val:
                return original
            r = dfs(original.right)
            if l:
                steps.append(-1)
                return l
            if r:
                steps.append(1)
                return r
        dfs(original)
        for i in steps[::-1]:
            if i == -1:
                cloned = cloned.left
            if i == 1:
                cloned = cloned.right
        return cloned