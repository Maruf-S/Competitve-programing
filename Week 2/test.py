# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printLinked(l):
    while l:
        print(l.val, end=" -> ")
        l = l.next
    print("None")

# def doStuff(head):
#     if(head == None):
#         # B case
#         return None
#     node = doStuff(head.next)
#     print(head.val)

# 1->2->3
# def reverseList(head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """
#     if head == None or head.next == None:
#         # No sub problem
#         # Return None or the head
#         return head

#     # New head is the last element w recursion law(Top of the c-stack)
#     newHead = reverseList(head.next)

#     head.next.next = head
#     head.next = None

#     return newHead


def isPalindrome(head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        # rev, rev.next, slow = slow, rev, slow.next
        # temp1 = slow
        # temp2 = rev
        # temp3 = slow.next
        # rev = temp1
        # rev.next = temp2
        # slow = temp3
        temp1 = slow
        temp2 = rev
        temp3 = slow.next
        rev = temp1
        rev.next = temp2
        slow = temp3
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev


x = ListNode(0, None)
y = x
for i in [1,2,2,1]:
    y.next = ListNode(i, None)
    y = y.next

print(isPalindrome(x.next))
