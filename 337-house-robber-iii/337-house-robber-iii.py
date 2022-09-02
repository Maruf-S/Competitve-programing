# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0,0]
            l = dfs(root.left)
            r = dfs(root.right)
            wroot = root.val + l[1] + r[1]
            woroot = max(l) + max(r)
            return [wroot,woroot]
        res = dfs(root)
        return max(res)