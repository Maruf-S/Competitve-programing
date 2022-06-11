# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def getKth(node,k):
            while k>0:
                if(not node):
                    return node
                node = node.next
                k-=1
            return node
        
        dummy = ListNode(0,head)
        prevGroupLast = dummy
        while True:
            kth = getKth(prevGroupLast,k)
            if(not kth):
                break
            groupNxt = kth.next
            # Reverse
            prev = groupNxt
            cur = prevGroupLast.next
            while cur!=groupNxt:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            temp = prevGroupLast.next
            prevGroupLast.next = kth
            prevGroupLast = temp
        return dummy.next
            