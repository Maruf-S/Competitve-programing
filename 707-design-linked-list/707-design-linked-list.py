class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode(0, None)
        self.length = 0

    def get(self, index: int) -> int:
        head = self.dummy.next
        if(index > self.length-1):
            return -1
        i = 0
        while(i < index):
            head = head.next
            i += 1
        return head.val

    def addAtHead(self, val: int) -> None:
        self.dummy.next = ListNode(val, self.dummy.next)
        self.length += 1

    def addAtTail(self, val: int) -> None:
        head = self.dummy.next
        if(head):
            while(head.next):
                head = head.next
            head.next = ListNode(val)
        else:
            self.dummy.next = ListNode(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if(index == self.length):
            return self.addAtTail(val)
        if(index >= self.length):
            return -1
        i = 0
        head = self.dummy
        while i < index:
            head = head.next
            i += 1
        nextEle = head.next
        head.next = ListNode(val, nextEle)
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if(index > self.length-1):
            return
        head = self.dummy
        i = 0
        while i < index:
            head = head.next
            i += 1
        head.next = head.next.next
        self.length -= 1