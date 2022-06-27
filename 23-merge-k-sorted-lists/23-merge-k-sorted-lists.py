# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        l,r = self.mergeKLists(lists[:len(lists)//2]),self.mergeKLists(lists[len(lists)//2:])
        return self.mergeTwoLists(l,r)
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()
        
        while list1 and list2:
            if(list1.val > list2.val):
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next
            head = head.next
        if(list1 or list2):
            head.next = list1 or list2
        return dummy.next