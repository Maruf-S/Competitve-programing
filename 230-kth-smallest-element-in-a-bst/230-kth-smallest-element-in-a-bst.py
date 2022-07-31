# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        r = []
        while root or s:
            while root:
                s.append(root)
                root = root.left
            node = s.pop()
            r.append(node.val)
            root = node.right
        return r[k-1]