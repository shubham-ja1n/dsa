# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    flag = [True]
    def depth(node):
        if node is None:
            return 0
        left_height = depth(node.left)
        right_height = depth(node.right)
        if abs(left_height-right_height) > 1:
            flag[0] = False
        return 1+ max(left_height, right_height)
    depth(root)
    return flag[0]