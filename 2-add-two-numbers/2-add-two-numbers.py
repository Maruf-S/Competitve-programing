class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 is None and l2 is None and carry == 0:
            return None
        
        val_1 = 0 if l1 is None else l1.val
        val_2 = 0 if l2 is None else l2.val
        
        val_sum = val_1 + val_2 + carry
        next_carry = 1 if val_sum > 9 else 0
        
        digit = val_sum % 10
        result_node = ListNode(digit)
        
        next_1 = None if l1 is None else l1.next
        next_2 = None if l2 is None else l2.next
        
        result_node.next = self.addTwoNumbers(next_1, next_2, next_carry)
        return result_node