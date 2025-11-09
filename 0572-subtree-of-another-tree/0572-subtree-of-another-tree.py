# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
return if the root contains the subroot

make a function that checks if the trees are identical
use a dfs algorithm

in main function check if the trees at the current postion are identical
if not move the the left tree or right tree and check again
'''
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False

        if root and subRoot and root.val == subRoot.val:
            return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)

