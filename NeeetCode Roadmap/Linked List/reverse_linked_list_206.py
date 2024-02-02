# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    return prev