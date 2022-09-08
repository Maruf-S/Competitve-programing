class Solution:
    def countNodes(self, root):
        leftdepth = self.getdepth(root, True)
        rightdepth = self.getdepth(root, False)

        if leftdepth == rightdepth:
            return 2 ** leftdepth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def getdepth(self, root, isLeft):
        if root is None:
            return 0
        if isLeft:
            return 1 + self.getdepth(root.left, isLeft)
        else:
            return 1 + self.getdepth(root.right, isLeft)
