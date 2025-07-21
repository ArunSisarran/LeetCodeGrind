# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if not root:
                return []

            return inorder(root.left) + [root.val] + inorder(root.right)

        sorted_vals = inorder(root)

        return sorted_vals[k - 1]