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


def mergeTwoLists(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    


x = ListNode(0, None)
y = x
z = ListNode(0, None)
m = z
for i in range(1, 15):
    if(i % 2):
        y.next = ListNode(i, None)
        y = y.next
    else:
        m.next = ListNode(i, None)
        m = m.next
# doStuff(x.next)

printLinked(mergeTwoLists(x.next, z.next))
