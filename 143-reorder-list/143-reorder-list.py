# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse list
        pre = None
        cur = slow.next
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        slow.next = None
        while pre:
            temp1 = head.next
            temp2 = pre.next
            head.next = pre
            pre.next = temp1

            pre = temp2
            head = temp1