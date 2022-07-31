# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            def isMirror(n1,n2):
                if not n1 and not n2:
                    return True
                if not n1 or not n2:
                    return False
                if n1.val == n2.val:
                    return isMirror(n1.left,n2.right) and isMirror(n1.right,n2.left)
                return False
            if not root:
                return True
            return isMirror(root.left,root.right)