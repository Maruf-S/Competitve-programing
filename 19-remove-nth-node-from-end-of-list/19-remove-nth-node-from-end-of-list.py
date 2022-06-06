# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        res = ListNode(0,head)
        right = head
        left = res
        for i in range(n-1):
            right = right.next
            
        print(right.val)
        while right and right.next:
            right = right.next
            left = left.next
        left.next = left.next.next
        return res.next