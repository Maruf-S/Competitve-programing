# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        res = float("inf")
        s = []
        while root or s:
            while root:
                s.append(root)
                root = root.left
            node = s.pop()
            if prev:
                res = min(res,node.val - prev.val)
            prev = node
            root = node.right
        return res