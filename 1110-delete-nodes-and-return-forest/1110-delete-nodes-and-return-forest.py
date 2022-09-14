class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        deleteSet = set(to_delete)
        res = []
        def dfs(root, par):
            if root is None:
                return None
            
            if root.val in deleteSet:
                dfs(root.left, None)
                dfs(root.right, None)
                return None
            
            root.left = dfs(root.left, root)
            root.right = dfs(root.right, root)
            if par is None:
                res.append(root)
                return
            return root
                  
        dfs(root, None)
        return res