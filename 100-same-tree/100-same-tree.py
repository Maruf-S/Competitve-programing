# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(n1,n2):
            if not n1 and not n2:
                return True
            elif not n2 or not n1:
                return False
            elif n1.val != n2.val:
                return False
            return check(n1.left,n2.left) and check(n1.right,n2.right)
        return check(q,p)