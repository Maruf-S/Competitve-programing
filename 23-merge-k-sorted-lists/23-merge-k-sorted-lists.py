class Solution:
    def mergeKLists(self, lists) -> ListNode:
        head = ListNode(None)
        curr = head
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                # lists[i] = lists[i].next

        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i].next:
                heapq.heappush(h, (lists[i].next.val, i))
                lists[i] = lists[i].next

        return head.next
