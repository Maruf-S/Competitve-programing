    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
class Solution(object):
    def reverseList(self,head):
        if not head:
            return None
        # Head(top) of the to be reversed sub problem
        newHead = head
        if(head.next):
            # There is a sub prob
            # Think of 2->3->None on head(2) head(3) gets returned because after the subprob is reversed
            # that is the top Node
            newHead = self.reverseList(head.next)
            # head.next was the 'next' element to the 'head' before the list was reversed
            # but it is now the last element of the reversed list and it points to null
            head.next.next = head
            head.next = None
        # If no sub prob return the only node or if there is a sub prob return the head
        return newHead
      