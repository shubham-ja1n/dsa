# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        if node:
            queue.append(node.left)
            queue.append(node.right)
            node.left, node.right = node.right, node.left
    
    return root