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

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = self.inorder_traversal(root)
        print(res)

        return res[k - 1] 