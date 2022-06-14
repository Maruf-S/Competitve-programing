# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, node: Optional[ListNode]) -> Optional[ListNode]:
            if(not node or not node.next):
                return node

            # left = node
            # right, fast = node, node.next
            # while fast and fast.next:
            #     fast = fast.next.next
            #     right = right.next
            # temp = right.next
            # right.next = None
            # right = temp

            left = node
            pre,right,fast = None,node,node
            while fast and fast.next:
                fast = fast.next.next
                pre = right
                right = right.next
            pre.next = None

            leftList = self.sortList(left)
            rightList = self.sortList(right)

            dummy = cur = ListNode(0)
            while leftList and rightList:
                if(leftList.val < rightList.val):
                    cur.next = leftList
                    cur = cur.next
                    leftList = leftList.next
                else:
                    cur.next = rightList
                    cur = cur.next
                    rightList = rightList.next
            cur.next = leftList or rightList
            return dummy.next