# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoSortedLists(self,l1,l2):
                head = dummy = ListNode()
                while l1 and l2:
                    if l1.val < l2.val:
                        dummy.next = l1
                        l1 = l1.next
                    else:
                        dummy.next = l2
                        l2 = l2.next
                    dummy = dummy.next
                if l1 or l2:
                    dummy.next = l1 or l2
                return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
                if len(lists) == 1:
                    return lists[0]
                if len(lists) == 0:
                    return None
                if len(lists) == 2:
                    return self.mergeTwoSortedLists(lists[0],lists[1])
                l,r = self.mergeKLists(lists[:len(lists)//2]),self.mergeKLists(lists[len(lists)//2:])
                return self.mergeTwoSortedLists(l,r)