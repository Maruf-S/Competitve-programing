# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        tsum = 0
        def dfs(node,path):
            nonlocal tsum
            if not node:
                return
            if not node.left and not node.right:
                tsum += int(path+str(node.val))
            dfs(node.left,path + str(node.val))
            dfs(node.right,path + str(node.val))
        dfs(root,"")
        return tsum