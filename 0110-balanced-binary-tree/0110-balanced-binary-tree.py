# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
determine if the binary tree is height balanced meaning the left and 
right subtrees do not differ by more than 1 in their height

use a dfs algorithm
check the height of the left sub tree
check the height of the right sub tree
if the abs(left - right) > 1 than its not height balanced
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            depth = 1 + max(left, right)

            if abs(left - right) > 1:
                self.balanced = False

            return depth

        dfs(root)
        return self.balanced

