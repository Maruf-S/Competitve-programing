"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        q = deque([root])
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                for i in node.children:
                    q.append(i)
                    temp.append(i.val)
            if temp:
                res.append(temp)
                
        return res