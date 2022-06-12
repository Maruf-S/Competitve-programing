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
                if(prev.val < current):
                    head = head.next
                    prev = prev.next
                else:
                    iterate = start
                    while iterate != head:
                        if iterate.val > current:
                            temp = iterate.val
                            iterate.val = current
                            head.val = temp
                            current = temp
                        iterate = iterate.next
                    head = head.next
                    prev = prev.next
            return dummy.next