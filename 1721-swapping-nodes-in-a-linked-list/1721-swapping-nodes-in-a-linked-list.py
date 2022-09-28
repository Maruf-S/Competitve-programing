# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        
        for _ in range(k):
            left = left.next
        temp = left
        
        leftp = dummy
        
        while left:
            left = left.next
            leftp = leftp.next
        temp.val,leftp.val = leftp.val,temp.val
        return dummy.next