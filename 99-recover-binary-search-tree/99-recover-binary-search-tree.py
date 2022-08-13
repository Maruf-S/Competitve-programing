# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        s = []
        prevele,first,second = None,None,None
        drops = []
        while s or root:
            while root:
                s.append(root)
                root = root.left
            node = s.pop()
            if prevele and not first and prevele.val > node.val:
                first = prevele
            if first and prevele.val > node.val:
                second = node
            prevele = node
            root = node.right
        first.val,second.val = second.val,first.val
        

        