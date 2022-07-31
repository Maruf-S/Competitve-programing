# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        r = []
        flag = True
        while q:
            temp = deque([])
            for i in range(len(q)):
                node  = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                temp.append(node.val) if flag else temp.appendleft(node.val)
            r.append(temp)
            flag= not flag
        return r