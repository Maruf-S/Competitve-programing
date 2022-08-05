# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.s = []
        self.moveL()
    def next(self) -> int:
        node = self.s.pop()
        self.root = node.right
        self.moveL()
        return node.val
    def hasNext(self) -> bool:
        return self.s or self.root
    def moveL(self):
        if self.s or self.root:
            while self.root:
                self.s.append(self.root)
                self.root = self.root.left
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()