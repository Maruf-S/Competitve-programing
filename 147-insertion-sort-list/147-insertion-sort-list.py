# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
            dummy = start = prev = ListNode(-5001, head)
            while head:
                current = head.val
                if prev.val > current:
                    iterate = start
                    while iterate != head:
                        if iterate.val > current:
                            temp = iterate.val
                            iterate.val = current
                            head.val = temp
                            current = temp
                        iterate = iterate.next
                prev = head
                head = head.next
            return dummy.next