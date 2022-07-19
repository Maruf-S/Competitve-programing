# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for i,j in enumerate(lists):
            if j:
                heapq.heappush(h,(j.val,i,j))
        dummy = head = ListNode()
        while h:
            v,i,n = heapq.heappop(h)
            head.next = n
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(h,(lists[i].val,i,lists[i]))
            head = head.next
        return dummy.next