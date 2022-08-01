# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        b = []
        def dfs(node,s):
            if not node:
                return
            dfs(node.left,s + str(node.val))
            if not node.left and not node.right:
                return b.append(s + str(node.val))
            dfs(node.right,s + str(node.val))
        dfs(root,"")
        return(sum(map(lambda x: int(str(int(x,2)),10),b)))