# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while root:
            if val > root.val:
                if root.right == None:
                    root.right = TreeNode(val)
                    return node
                root = root.right
            else:
                if root.left == None:
                    root.left = TreeNode(val)
                    return node
                root = root.left
        return TreeNode(val)