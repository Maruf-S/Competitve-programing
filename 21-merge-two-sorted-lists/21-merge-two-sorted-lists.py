# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self,l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if(l1.val < l2.val):
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        cur.next = l1 or l2
        return dummy.next
