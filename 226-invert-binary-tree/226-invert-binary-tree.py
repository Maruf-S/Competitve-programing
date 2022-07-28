# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert_child(node):
            if not node:
                return
            node.left,node.right = node.right,node.left
            invert_child(node.right)
            invert_child(node.left)
        node = root
        invert_child(node)
        return root