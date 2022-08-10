"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        otn = {}
        def dfs(node):
            if not node:
                return None
            if node in otn:
                return otn[node]
            cp = Node(node.val)
            otn[node] = cp
            cp.next = dfs(node.next)
            cp.random = dfs(node.random)
            return cp
        return dfs(head)