# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([[root,0]])
        res = 0
        while q:
            tempq = deque([])
            n = len(q)
            for i in range(n):
                node,pos = q.popleft()
                tempq.append(pos)
                if node.left:
                    q.append([node.left,(pos*2 )])
                if node.right:
                    q.append([node.right,(pos*2) + 1])
            res = max(res,tempq[-1] - tempq[0] + 1)
        return res
    