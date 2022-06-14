class ListNode():
    def __init__(self, key: int,val:int):
        self.key=key
        self.val= val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = ListNode(0,0),ListNode(0,0)
        self.left.left,self.right.prev = self.right,self.left
    def deleteNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def insertRight(self,node):
        rm = self.right.prev
        node.next = self.right
        node.prev = rm
        rm.next = node
        self.right.prev = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            self.insertRight(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.deleteNode(node)
            self.insertRight(node)
        else:
            node = ListNode(key,value)
            self.cache[key] = node
            self.insertRight(node)
            self.cap-=1
            
        if(self.cap<0):
            # Delete LRU
            lru = self.left.next
            self.deleteNode(lru)
            del self.cache[lru.key]
            self.cap+=1
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)