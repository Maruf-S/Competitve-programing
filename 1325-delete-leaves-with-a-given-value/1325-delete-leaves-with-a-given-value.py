# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return node
            # if not node.right and not node.left:
            #     if node.val == target:
            #         return None
            node.left = helper(node.left)
            node.right = helper(node.right)

            if not node.right and not node.left:
                if node.val == target:
                    return None
            return node
        return helper(root)