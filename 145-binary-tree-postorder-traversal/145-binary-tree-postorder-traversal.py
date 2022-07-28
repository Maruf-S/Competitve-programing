class Solution(object):
    def postorderTraversal(self, root):
        stack, r = [], []
        while stack or root:
            if root:
                r.append(root.val)
                stack.append(root)
                root = root.right
            else:
                root = stack.pop().left

        return r[::-1]