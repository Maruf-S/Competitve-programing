# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = defaultdict(lambda: float("-inf"))
        def dfs(node,lvl):
            if not node:
                return
            res[lvl] = max(node.val,res[lvl])
            dfs(node.left,lvl + 1)
            dfs(node.right,lvl + 1)
        dfs(root,0)
        return map(lambda x: x[1],sorted(list(res.items()),key= lambda x: x[0]))