# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        reg = None
        while fast and fast.next:
            fast = fast.next.next
            temp1 = slow
            temp2 = slow.next
            temp3 = reg
            reg = slow
            reg.next = temp3
            slow = temp2
        
        max_sum = 0
        while reg:
            max_sum = max(slow.val+reg.val,max_sum)
            reg = reg.next
            slow = slow.next
        return max_sum
        