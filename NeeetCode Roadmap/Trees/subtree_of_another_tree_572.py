# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSubtree(root, subRoot):
    """
    :type root: TreeNode
    :type subRoot: TreeNode
    :rtype: bool
    """
    if not subRoot:
        return True
    if not root:
        return False
    
    return (sameTree(root,subRoot) or 
    isSubtree(root.left, subRoot) or
    isSubtree(root.right, subRoot))

def sameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    
    return (sameTree(p.left, q.left) and 
    sameTree(p.right, q.right))