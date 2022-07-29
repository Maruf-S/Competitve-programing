# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s = []
        res = []
        while s or root:
            while root:
                s.append(root)
                root = root.left
            node = s.pop()
            res.append(node.val)
            root = node.right
        return res