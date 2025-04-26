# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Given the root of a binary tree and a sum
Find if the tree contains a path from root to leaf that adds to the sum
'''


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case, checking if there is a current node
        if not root:
            return False
        # If the current node does not have a left or right node it is a leaf
        if not root.left and not root.right:
            return targetSum - root.val == 0

        targetSum -= root.val
        # Recursively call the function to check the left and right subtrees
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        