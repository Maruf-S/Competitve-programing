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
        prevele  = TreeNode(float("-inf"))
        drops = []
        while s or root:
            while root:
                s.append(root)
                root = root.left
            node = s.pop()
            if prevele.val > node.val:
                drops.append((prevele,node))
            prevele = node
            root = node.right
        drops[0][0].val,drops[-1][1].val = drops[-1][1].val,drops[0][0].val