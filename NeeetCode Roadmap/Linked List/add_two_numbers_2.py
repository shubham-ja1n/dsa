# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = None
    tail = None
    carry = 0
    while l1 and l2:
        sum = l1.val + l2.val +carry
        val = sum % 10
        carry = sum // 10
        new_node = ListNode(val)
        if not head:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
        l1 = l1.next
        l2 = l2.next
    
    while l1:
        sum = l1.val + carry
        val = sum % 10
        carry = sum // 10
        new_node = ListNode(val)
        tail.next = new_node
        tail = new_node
        l1 = l1.next
    
    while l2:
        sum = l2.val + carry
        val = sum % 10
        carry = sum // 10
        new_node = ListNode(val)
        tail.next = new_node
        tail = new_node
        l2 = l2.next
    
    if carry !=0:
        new_node = ListNode(carry)
        tail.next = new_node
        tail = new_node
    return head