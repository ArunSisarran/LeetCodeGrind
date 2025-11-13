# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Find the lowest common ancestor in the tree and return it

This is a binary search tree meaning it follows a structure that orders the 
nodes, if any node is smaller than the current root its in the left subtree
any node bigger in the right subtree, the lowest common ancestor would be the node
that the p and q are not both bigger or smaller than.
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root
        