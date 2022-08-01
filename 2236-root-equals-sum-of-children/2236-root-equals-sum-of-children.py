# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        return root.val ==  self.checkTree(root.left) + self.checkTree(root.right)
        