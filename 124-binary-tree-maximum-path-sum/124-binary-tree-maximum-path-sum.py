# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return [-inf,0]
            l = dfs(node.left)
            r = dfs(node.right)
            
                  # With # Without
            res = [-inf,-inf]
            res[0] = max(l[0],r[0],node.val,node.val + l[1] + r[1], node.val + max(l[1],r[1]))
            res[1] = max(node.val + max(l[1],r[1]),node.val)
            return res
        # print(dfs(root))
        return max(dfs(root))