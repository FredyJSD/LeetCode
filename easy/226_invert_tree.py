# Given the root of a binary tree, invert the tree, and return its root.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def invertTree(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: Optional[TreeNode]
    """
    if root is None:
        return None
    
    temp = root.left
    root.left = root.right
    root.right = temp

    invertTree(root.left)
    invertTree(root.right)

    return root


#Base case is to return if the value of current node is None
#Start by swapping every node on the left
#The swap every node on the right
    
    