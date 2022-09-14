# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def isPsudoPalind(count):
            oddcount = 0
            for i in count.values():
                oddcount += i % 2 != 0
                if oddcount > 1:
                    return False
            return True
        def dfs(node,count):
            if not node:
                return 0
            count = dict(count)
            count[node.val] = count.get(node.val,0) + 1
            
            if not node.left and not node.right:
                if isPsudoPalind(count):
                    return 1
                else:
                    return 0
            return dfs(node.left,count) + dfs(node.right,count)
        return dfs(root,dict())