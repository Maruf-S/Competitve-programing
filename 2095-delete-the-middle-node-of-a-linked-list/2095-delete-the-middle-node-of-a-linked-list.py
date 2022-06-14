# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head.next):
            return None
        dummy = ListNode(0,head)
        fast,slow = head,head
        pre = None
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        print(slow.val)
        print(pre.val)
        pre.next = pre.next.next
        return dummy.next