# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        s = []
        while root or s:
            while root:
                res.append(root.val)
                s.append(root)
                root = root.left
            root = s.pop()
            root = root.right
        return res