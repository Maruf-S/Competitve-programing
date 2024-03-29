# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        dummy = ListNode(-5001, head)
        #Cur
        prev = head
        head = head.next
        while head:
            current = head.val
            if(prev.val < current):
                prev = head
                head = head.next
            else:
                temp = dummy
                while current > temp.next.val and temp != head:
                    temp = temp.next
                curEle = head
                nextEle = head.next
                #! Deattach head
                prev.next = head.next
                #!
                head.next = temp.next
                temp.next = head

                head = nextEle
                # Prev doesn't change because the curr element is removed
        return dummy.next
