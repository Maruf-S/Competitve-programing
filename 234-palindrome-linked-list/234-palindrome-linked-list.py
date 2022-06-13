# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            temp1 = slow
            temp2 = rev
            temp3 = slow.next
            rev = temp1
            rev.next = temp2
            slow = temp3
        if fast:
            #Skip the middle element(odd no of elements)
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev