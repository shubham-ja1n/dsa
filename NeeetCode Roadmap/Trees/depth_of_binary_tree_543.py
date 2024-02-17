# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def diameterOfBinaryTree(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    diameter = [0]

    def depth(node):
        if node is None:
            return 0
        left_height = depth(node.left)
        right_height = depth(node.right)
        diameter[0] = max(diameter[0], left_height+right_height)

        return 1+ max(left_height, right_height)
    
    depth(root)

    return diameter[0]