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
        cur = root
        while cur or s:
            while cur:
                s.append(cur)
                cur = cur.left
            cur = s.pop()
            res.append(cur.val)
            cur= cur.right
        return res