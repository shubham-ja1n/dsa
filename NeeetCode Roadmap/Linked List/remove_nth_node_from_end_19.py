def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    prev=None
    slow = fast = head
    for _ in range(n):
        fast = fast.next
    
    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next
    if prev:
        prev.next = slow.next
        slow.next = None
        return head
    else:
        return head.next