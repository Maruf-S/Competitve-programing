# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def calcDepth(node,dep):
            if not node:
                return
            nonlocal depth
            depth = max(dep,depth)
            calcDepth(node.left,dep + 1)
            calcDepth(node.right,dep + 1)

        calcDepth(root,1)
        return depth