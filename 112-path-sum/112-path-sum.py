# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node,cursum):
            if not node:
                return False
            if not node.left and not node.right:
                if targetSum == cursum + node.val:
                    return True
            return dfs(node.left,cursum + node.val) or dfs(node.right,cursum + node.val)
        
        return dfs(root,0)