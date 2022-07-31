# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level = 0
        minlevel = 0
        maxsum = float("-inf")
        
        while q:
            level += 1
            lvlsum = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                lvlsum.append(node.val)
            lvls = sum(lvlsum)
            if lvls > maxsum:
                maxsum = lvls
                minlevel = level
        return minlevel