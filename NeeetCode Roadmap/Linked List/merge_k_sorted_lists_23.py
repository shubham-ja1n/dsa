# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        mergedLists =[]
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if (i+1) < len(lists) else None
            mergedLists.append(merge(l1,l2))
        lists = mergedLists
    
    return lists[0]

def merge(list1, list2):
    dummy = ListNode()
    temp = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next
    
    if list1:
        temp.next = list1
    
    if list2:
        temp.next = list2
    return dummy.next