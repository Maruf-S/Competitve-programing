# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        count = 0
        def dfs(node,cur):
                nonlocal count
                if not node:
                    return
                cur += node.val
                count += d[cur - targetSum]
                d[cur] += 1
                dfs(node.left,cur)
                dfs(node.right,cur)
                d[cur] -= 1
        dfs(root,0)
        return count