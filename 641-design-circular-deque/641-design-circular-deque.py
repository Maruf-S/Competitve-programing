class Node:
    def __init__(self,val,nxt,prev):
        self.val,self.nxt,self.prev = val,nxt,prev
class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.max = k
        self.items = 0
        self.left = Node(None,None,None)
        self.right = Node(None,None,self.left)

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if(self.isFull()):return False
        if(self.isEmpty()):
            cur = Node(value,self.right,self.left)
            self.left.nxt = cur
            self.right.prev = cur
        else:
            cur = Node(value,self.left.nxt,self.left)
            self.left.nxt.prev = cur
            self.left.nxt = cur
        self.items += 1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if(self.isFull()):return False
        if(self.isEmpty()):
            cur = Node(value,self.right,self.left)
            self.left.nxt = cur
            self.right.prev = cur
        else:
            cur = Node(value,self.right,self.right.prev)
            self.right.prev.nxt = cur
            self.right.prev = cur
        self.items +=1
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if(self.isEmpty()):return False
        self.left.nxt.nxt.prev = self.left
        self.left.nxt = self.left.nxt.nxt
        self.items-=1
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if(self.isEmpty()):return False
        self.right.prev.prev.nxt = self.right
        self.right.prev = self.right.prev.prev
        self.items -= 1
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if(self.isEmpty()):
            return -1
        return self.left.nxt.val
    def getRear(self):
        """
        :rtype: int
        """
        if(self.isEmpty()):
            return -1
        return self.right.prev.val

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.items <= 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.items >= self.max
