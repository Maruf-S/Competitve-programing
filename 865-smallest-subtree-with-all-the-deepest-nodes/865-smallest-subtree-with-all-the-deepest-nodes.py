# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def depth(node):
            if not node:
                return 0, None
            l = depth(node.left)
            r = depth(node.right)
            if l[0] > r[0]:
                return l[0]+1, l[1]
            elif l[0] < r[0]:
                return r[0]+1, r[1]
            else:
                return l[0] + 1, node
        return depth(root)[1]