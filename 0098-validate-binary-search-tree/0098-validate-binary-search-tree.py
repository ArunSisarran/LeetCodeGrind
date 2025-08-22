# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder_traversal(self, root):
        if not root:
            return []

        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = self.inorder_traversal(root)

        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False
        return True
