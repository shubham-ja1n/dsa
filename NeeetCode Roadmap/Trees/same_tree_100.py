# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    queue = deque()
    queue.append((p,q))
    while queue:
        node1, node2 = queue.popleft()
        if node1 and node2:
            if node1.val!=node2.val:
                return False
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        elif node1:
            return False
        elif node2:
            return False
    return True