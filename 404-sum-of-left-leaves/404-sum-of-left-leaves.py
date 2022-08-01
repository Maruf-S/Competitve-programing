# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        if node.left and node.left.left == None and not node.left.right:
            return node.left.val + self.sumOfLeftLeaves(node.right)
        else:
            return self.sumOfLeftLeaves(node.left) + self.sumOfLeftLeaves(node.right)