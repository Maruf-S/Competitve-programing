# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        dummy = TreeNode(preorder[0])
        s = [dummy]
        for i in preorder[1:]:
            if i < s[-1].val:
                node = TreeNode(i)
                s[-1].left = node
                s.append(node)
            else:
                last = None
                while s and i > s[-1].val:
                    last = s.pop()
                    
                last.right = TreeNode(i)
                s.append(last.right)
        return dummy