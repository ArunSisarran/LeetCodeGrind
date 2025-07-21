# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Solution makes sense because if both values are bigger than the root then go in the right subtree,
if both values are smaller than root then its in the left subtree. And if one is bigger and one is smaller
then the current node is the descendent 
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


        