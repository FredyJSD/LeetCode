# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# Base cases make sure to check if the node is the same or not
# Base cases return false if the nodes do not match
# Recursivley checks left node and then right node
    