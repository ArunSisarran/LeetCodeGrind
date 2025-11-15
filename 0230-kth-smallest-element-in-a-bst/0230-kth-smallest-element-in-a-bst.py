# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
return the smallest k values of the binary tree
'''
class Solution:
    def inorder(self, root):
        if not root:
            return []
        while root:
            return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = self.inorder(root)
        return res[k - 1]
        
        