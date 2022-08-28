# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        s = []
        while s or root:
            while root:
                s.append(root)
                root = root.left
            node = s.pop()
            arr.append(node.val)
            root = node.right
        
        def makeTree(arr):
            if not arr:
                return None
            m = len(arr)//2
            root = TreeNode(arr[m])
            root.left = makeTree(arr[:m])
            root.right = makeTree(arr[m + 1 :])
            return root
        return makeTree(arr)