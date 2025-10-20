# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # helper function that determines if both trees have the same nodes
    def same(self, root, subroot):
        if not root and not subroot:
            return True

        if (root and subroot) and (root.val == subroot.val):
            return (self.same(root.left, subroot.left) and self.same(root.right, subroot.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if not subRoot:
            return True

        # check if the current root is the same as the subRoot
        if self.same(root, subRoot):
            return True

        # recursively call this on the left and right trees to check is the subroot is in there
        # we use or because the subroot can be in either the left or right subtree
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        