# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root
        def findPred(node):
            cur = node.left
            while cur.right and cur.right != node:
                cur = cur.right
            return cur
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pred = findPred(cur)
                if not pred.right:
                    pred.right = cur
                    cur = cur.left
                else:
                    # res.append(cur.val)
                    # cur = cur.right
                    # pred.right = None
                    cur.left = None
        return res
