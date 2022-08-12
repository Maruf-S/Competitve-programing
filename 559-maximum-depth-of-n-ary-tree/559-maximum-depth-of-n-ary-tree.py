"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        maxh = 0
        
        def dfs(node,h):
            nonlocal maxh
            if not node:
                return
            if not node.children:
                maxh = max(maxh,h + 1)
                return
            for n in node.children:
                dfs(n,h + 1)
        dfs(root,0)
        return maxh