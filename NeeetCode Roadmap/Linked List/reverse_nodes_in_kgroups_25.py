# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    dummy = ListNode(0, head)
    groupPrev = dummy
    while True:
        kth = getkth(groupPrev, k)
        if kth:
            groupNext = kth.next

            prev, curr = groupNext, groupPrev.next

            while not curr == groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp
        else:
            break
    return dummy.next

def getkth(curr, k):
    while curr and k >0:
        curr = curr.next
        k -= 1
    return curr