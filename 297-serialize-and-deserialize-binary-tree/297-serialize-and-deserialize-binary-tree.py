# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = []
        
        def spreord(node):
            if not node:
                s.append("None")
                return
            s.append(str(node.val))
            spreord(node.left)
            spreord(node.right)
        spreord(root)
        return ",".join(s)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            if data[i] == "None":
                i += 1
                return None
            node = TreeNode(int(data[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))