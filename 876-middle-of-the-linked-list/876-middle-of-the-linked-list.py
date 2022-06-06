# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 0
        ic = head
        
        while(ic):
            i+=1
            ic = ic.next
        j = (i//2)+1
        i = 1
        print(j)
        while(i<j):
            head= head.next
            i+=1
        return head