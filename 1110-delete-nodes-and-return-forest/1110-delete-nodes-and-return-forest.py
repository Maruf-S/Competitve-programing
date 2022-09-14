# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        td = set(to_delete)
        def dfs(node):
            if not node:
                return False
            p = False
            if node.val in td:
                p = True
                if node.left and node.left.val not in td:
                    res.append(node.left)
                if node.right and node.right.val not in td:
                    res.append(node.right)
            if dfs(node.left):
                node.left = None
            
            if dfs(node.right):
                node.right = None
            return p
        if root.val not in td:
            res.append(root)
        dfs(root)
        return res